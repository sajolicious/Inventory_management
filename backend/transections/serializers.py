from .models import Suppliers,PurchaseBill,User,PurchaseItem,PurchaseBillDetails,SaleBill
from rest_framework import serializers
class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Suppliers
        fields=['id','name','phone','address','email']
        lookup_field=['id']
    def create(self, validated_data):
        related_name = validated_data.pop('created_by', None)
        instance = Suppliers.objects.create(**validated_data)
        if related_name:
            # Do something with the related_name field, such as creating a related object
            pass
        return instance
class SuppliersSerializerLogin(serializers.ModelSerializer):
    class Meta:
        model=Suppliers
        fields=['name','email']
class PurchseBillSerializer(serializers.ModelSerializer):
    billobj=serializers.CharField(read_only=True)
    class Meta:
        model=PurchaseBill
        fields=['bill','purchase_time','suppliers','billobj']
class PurchseItemSerializer(serializers.ModelSerializer):
    billobj=serializers.CharField(read_only=True)
    class Meta:
        model=PurchaseBill
        fields=['bill','stock','perprice','quantity','totalprice']
