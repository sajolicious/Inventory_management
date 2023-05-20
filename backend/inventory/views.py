from django.shortcuts import render
from .models import stock
from .serializers import StockSerializer
from rest_framework import viewsets
# Create your views here.
class StockListView(viewsets.ModelViewSet):
    queryset=stock.objects.all()
    serializer_class=StockSerializer