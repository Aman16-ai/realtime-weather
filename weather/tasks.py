from celery import shared_task
import requests
from .models import WeatherData, DailyWeatherSummary
from django.conf import settings
from datetime import datetime, timedelta
from django.db.models import Avg, Max, Min, Count

@shared_task
def fetch_weather_data():
    api_key = "your_api_key"
    metros = {
        "Delhi" : [28.6517178,77.2219388],
        "Mumbai" : [19.0785451,72.878176]
    }
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format

    for m in metros.keys():
        lat = metros[m][0]
        lon = metros[m][1]
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=ef6b766d67d6a493fa05af0eb5a5ef8a"
        response = requests.get(url)
        data = response.json()
        timestamp = datetime.utcfromtimestamp(data['dt'])
        weatherData = WeatherData(
                city=m,
                main=data['weather'][0]['main'],
                temp=round(data['main']['temp'] - 273.15,2),  # Convert Kelvin to Celsius
                feels_like=round(data['main']['feels_like'] - 273.15,2),
                timestamp=timestamp
            )
        weatherData.save()
        print(weatherData)

@shared_task
def calculate_daily_summary():
    

    cities = ["Delhi", "Mumbai"]
    for city in cities:
        data = WeatherData.objects.filter(city=city, timestamp__date=datetime.now().date())
        if data.exists():
            avg_temp = data.aggregate(Avg('temp'))['temp__avg']
            max_temp = data.aggregate(Max('temp'))['temp__max']
            min_temp = data.aggregate(Min('temp'))['temp__min']
            dominant_weather = data.values('main').annotate(weather_count=Count('main')).order_by('-weather_count')[0]['main']

            DailyWeatherSummary.objects.create(
                city=city,
                date=datetime.now().date(),
                avg_temp=avg_temp,
                max_temp=max_temp,
                min_temp=min_temp,
                dominant_weather=dominant_weather
            )
