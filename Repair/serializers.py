from rest_framework.serializers import ModelSerializer
from .models import Repair


class RepairSerializer(ModelSerializer):
    class Meta:
        model = Repair
        fields = '__all__'
        