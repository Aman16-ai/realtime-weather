from django.contrib import admin
from .models import WeatherData,DailyWeatherSummary
# Register your models here.
admin.site.register((WeatherData,DailyWeatherSummary))