from rest_framework.response import Response
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import authenticate


@csrf_exempt
@permission_classes([AllowAny])
@api_view(["GET", "POST"])
def UserRegistration(request):
    users = CustomUser.objects.all()
    serializer = RegisterSerializer(users, many=True)
    if request.method == 'POST':
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return Response(serializer.data, status=status.HTTP_200_OK)
    


@api_view(["POST"])
@permission_classes([AllowAny])
def user_login(request):
    """Authenticate user and return JWT tokens."""
    email = request.data.get("email")
    password = request.data.get("password")
    user = authenticate(email=email, password=password)

    if user is None:
        return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)
    
    login(request, user)
   
    refresh = RefreshToken.for_user(user)
    print("refresh", refresh)
    return Response({
        "email": user.email,
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def user_logout(request):
    """Logout user and blacklist the refresh token."""
    try:
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


