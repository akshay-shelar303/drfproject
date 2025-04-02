from rest_framework import serializers
from .models import LaptopSell

class LaptopSellSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptopSell
        fields = '__all__'