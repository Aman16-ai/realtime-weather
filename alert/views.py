from django.shortcuts import render

from rest_framework import viewsets
from .models import UserAlertConfig
from .serializers import UserAlertConfigSerializer

class UserAlertConfigViewSet(viewsets.ModelViewSet):
    queryset = UserAlertConfig.objects.all()
    serializer_class = UserAlertConfigSerializer
