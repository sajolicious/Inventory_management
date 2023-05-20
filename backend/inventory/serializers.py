from .models import stock
from rest_framework import serializers

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=stock
        fields=['id','name','description','quantity','price','created_at','updated_at','is_delated']
    
    