from django.shortcuts import render
from .models import LaptopSell
from .serializers import LaptopSellSerializer
from rest_framework.viewsets import ModelViewSet


class LaptopSellViewSet(ModelViewSet):
    queryset = LaptopSell.objects.all()
    serializer_class = LaptopSellSerializer
    