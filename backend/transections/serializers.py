from .models import Suppliers, PurchaseBill, PurchaseItem,PurchaseBillDetails
from rest_framework import serializers


class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = ('id', 'name', 'phone', 'address', 'email')
        lookup_field = 'id'

    def create(self, validated_data):
        related_name = validated_data.pop('created_by', None)
        instance = Suppliers.objects.create(**validated_data)
        if related_name:
            # Do something with the related_name field, such as creating a related object
            pass
        return instance


class SuppliersSerializerLogin(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = ('name', 'email')
class PurchaseBillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseBillDetails
        fields = '__all__'


class PurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = '__all__'

class PurchaseBillSerializer(serializers.ModelSerializer):
    purchItem = PurchaseItemSerializer(many=True)
    purchasedetailsbillno = PurchaseBillDetailsSerializer(many=True)

    class Meta:
        model = PurchaseBill
        fields = '__all__'

    def create(self, validated_data):
        purchase_items_data = validated_data.pop('purchItem')
        purchase_details_data = validated_data.pop('purchasedetailsbillno')

        purchase_bill = PurchaseBill.objects.create(**validated_data)

        for item_data in purchase_items_data:
            PurchaseItem.objects.create(bill=purchase_bill, **item_data)

        for detail_data in purchase_details_data:
            PurchaseBillDetails.objects.create(billno=purchase_bill, **detail_data)

        return purchase_bill
class PurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = ('id', 'stock', 'quantity', 'perprice', 'totalprice')


