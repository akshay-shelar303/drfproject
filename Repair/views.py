from django.shortcuts import render
from .models import Repair
from .serializers import RepairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


class RepairList(APIView):
    def get(self, request):
        repairs = Repair.objects.all()
        paginator = PageNumberPagination()
        paginated_queryset = paginator.paginate_queryset(repairs, request)
        serializer = RepairSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = RepairSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RepairUpdateDetail(APIView):
    def get(self, request, pk):
        repair = Repair.objects.get(id=pk)
        serializer = RepairSerializer(repair)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        repair = Repair.objects.get(id=pk)
        serializer = RepairSerializer(repair, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        repair = Repair.objects.get(id=pk)
        repair.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)