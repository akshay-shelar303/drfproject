from django.urls import path
from .views import UserRegistration, UserLogin


urlpatterns = [
    path('register/', UserRegistration, name='user-registration'),
]