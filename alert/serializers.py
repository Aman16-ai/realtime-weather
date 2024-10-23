# serializers.py
from rest_framework import serializers
from .models import UserAlertConfig

class UserAlertConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAlertConfig
        fields = ['id', 'user_email', 'temp_threshold', 'city'] 
