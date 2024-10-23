from django.db import models
from weather.models import WeatherData
# Create your models here.

class UserAlertConfig(models.Model):
    user_email = models.EmailField()
    temp_threshold = models.IntegerField(default=30)
    city = models.CharField(default='None',max_length=50)
    def __str__(self) -> str:
        return self.user_email


class Alert(models.Model):
    config = models.ForeignKey(UserAlertConfig,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    weather = models.ForeignKey(WeatherData,on_delete=models.CASCADE)