from django.urls import path
from .views import UserRegistration, user_login, user_logout


urlpatterns = [
    path("register/", UserRegistration, name="user-registration"),
    path("login/", user_login, name="user-login"),
    path("logout/", user_logout, name="user-logout"),
]
