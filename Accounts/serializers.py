from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_technician', 'is_customer']



class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def validate(self, attrs):
        user = CustomUser.objects.filter(username=attrs['username']).first()
        if user and user.check_password(attrs['password']):
            return user
        raise serializers.ValidationError("Invalid username or password")