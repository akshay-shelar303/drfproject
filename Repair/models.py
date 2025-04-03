from django.db import models
# from django.contrib.auth.models import User
from Accounts.models import CustomUser

class Repair(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    customer_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15)
    laptop_model = models.CharField(max_length=255)
    issue_description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Technician handling the repair

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.laptop_model} - {self.status}"
