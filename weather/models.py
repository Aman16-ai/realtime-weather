from django.db import models
# Create your models here.
# models.py
from django.db import models
from datetime import datetime,timedelta
from django.utils import timezone
from django.db.models import Count

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    main = models.CharField(max_length=100)
    temp = models.FloatField()
    feels_like = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.city} temperature at {self.timestamp.date()} is {self.temp}"
    
    @classmethod
    def getLatestWeatherOfCity(cls,city_name):
        return WeatherData.objects.filter(city=city_name).latest("timestamp")
    
    @classmethod
    def getTodayWeatherTrendOfCity(cls,city_name):
        return WeatherData.objects.filter(city=city_name,timestamp__date=datetime.today())
    

class DailyWeatherSummary(models.Model):
    city = models.CharField(max_length=100)
    date = models.DateField()
    avg_temp = models.FloatField()
    max_temp = models.FloatField()
    min_temp = models.FloatField()
    dominant_weather = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"Summary of {self.city} at {self.date}"
    
    @staticmethod
    def getDaysDominantWeatherOfCity(city_name,days=7):
        ago = timezone.now() - timedelta(days=days)
        return DailyWeatherSummary.objects.filter(city=city_name,date__gte = ago).values('dominant_weather').annotate(count=Count('dominant_weather'))
