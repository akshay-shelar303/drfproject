from django.urls import path
from .views import RepairList, RepairUpdateDetail


urlpatterns = [
    path('repairs/', RepairList.as_view()),
    path('repairs/<int:pk>/', RepairUpdateDetail.as_view()),
]