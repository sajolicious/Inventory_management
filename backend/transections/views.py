from .models import Suppliers, PurchaseBill, PurchaseItem, PurchaseBill, PurchaseItem, PurchaseBillDetails
from .serializers import SuppliersSerializerLogin, SuppliersSerializer, PurchaseItemSerializer, PurchaseBillSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect
from rest_framework.exceptions import NotFound
from inventory.models import stock
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class UserLogin(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializerLogin
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = SuppliersSerializerLogin(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def login(self, request):
        username = request.data.get('name')
        email = request.data.get('email')
        user = Suppliers.objects.filter(name=username).first()
        if user is None:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class SuppliersView(viewsets.ModelViewSet):
    queryset = Suppliers.objects.filter(is_deleted=False)
    serializer_class = SuppliersSerializer
    pagination_class = PageNumberPagination


class SuppliersCreateView(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        heders = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=heders)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class SupplierUpdateView(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer

    def update(self, request, pk=None):
        suppliers = self.get_object(pk)
        serializer = self.get_serializer(
            suppliers, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Suppliers.objects.get(pk=pk)
        except Suppliers.DoesNotExist:
            raise


class SupplierDelateView(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer

    def delate(self, request, pk=None):
        Suppliers = self.del_object(pk)
        Suppliers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def del_object(self, pk):
        try:
            return Suppliers.objects.get(pk=pk)
        except Suppliers.DoesNotExist:
            raise


class SupplierProfileView(viewsets.ReadOnlyModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer

    def retrive(self, request, pk=None):
        instance = self.get_object()

        profile_data = {
            'name': instance.name,
            'address': instance.address,
            'phone': instance.phone,
        }
        return Response(profile_data, status=status.HTTP_401_UNAUTHORIZED)

class PurchaseCreateView(viewsets.ModelViewSet):
    queryset = PurchaseBill.objects.all()
    serializer_class = PurchaseBillSerializer
  