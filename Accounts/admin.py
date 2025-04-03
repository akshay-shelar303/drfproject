from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_technician', 'is_customer')
    search_fields = ('username', 'email')


admin.site.register(CustomUser, CustomUserAdmin)