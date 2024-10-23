from rest_framework import serializers
from .models import DailyWeatherSummary, WeatherData


class DailyWeatherSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyWeatherSummary
        fields = "__all__"

        
class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherData
        fields = "__all__"