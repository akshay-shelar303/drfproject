from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CustomUser


class CustomUserAPITestCase(APITestCase):
    def setUp(self):
        # Create a user instance for testing
        self.user = CustomUser.objects.create_user(
            email="test@gmail.com",
            password="testpassword", name="Test User"
        )
        
    def test_get_user(self):
        response = self.client.get(f'/user/users/', format='json')
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["email"], "test@gmail.com")
        self.assertEqual(data[0]["name"], "Test User")