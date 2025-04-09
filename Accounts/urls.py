from django.urls import path

from .views import UserList, UserLogin, UserLogout, UserRegistration

urlpatterns = [
    path("register/", UserRegistration.as_view(), name="registration"),
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("users/", UserList.as_view(), name="user-list"),
]
