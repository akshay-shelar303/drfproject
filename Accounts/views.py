from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer, UserLoginSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(["GET", "POST"])
def UserRegistration(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    if request.method == 'POST':
            serializer = CustomUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return Response(serializer.data, status=status.HTTP_200_OK)
    


@api_view(["POST"])
def UserLogin(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)