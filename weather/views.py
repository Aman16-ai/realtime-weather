from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import DailyWeatherSummarySerializer, WeatherSerializer
from .models import DailyWeatherSummary,WeatherData
# Create your views here.



#viz -> date vs dominant_weather && date vs avg_temp/ min_temp/ max_temp

class DailyWeatherSummaryViewset(viewsets.ModelViewSet):
    queryset = DailyWeatherSummary.objects.all()
    serializer_class = DailyWeatherSummarySerializer
    # http_method_names = ['GET']
    def get_queryset(self):
        if 'city' in self.request.GET:
            return DailyWeatherSummary.objects.filter(city=self.request.GET['city']).order_by('-date')
        return super().get_queryset()
    
    def list(self, request, *args, **kwargs):
        if 'city' in self.request.GET and 'filter' in self.request.GET:
            obj = list(DailyWeatherSummary.getDaysDominantWeatherOfCity(city_name=self.request.GET['city'],days=7))
            print(obj)
            return Response(data=obj)
        return super().list(request, *args, **kwargs)
    


#viz -> current day vs main pie chart
class WeatherViewset(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherSerializer

    def get_queryset(self):
        if('city' in self.request.GET and 'filter' not in self.request.GET):
            return WeatherData.objects.filter(city=self.request.GET['city'])
        if 'city' in self.request.GET and self.request.GET['filter']=='today_trends':
            return WeatherData.getTodayWeatherTrendOfCity(self.request.GET['city'])
        return super().get_queryset()
    
    def list(self, request, *args, **kwargs):
        if 'city' in request.query_params and 'filter' in request.query_params:
            city = request.query_params['city']
            if request.query_params['filter'] == 'latest':
                latest_weather = WeatherData.getLatestWeatherOfCity(city)
                if latest_weather:
                    serializer = self.get_serializer(latest_weather)
                    return Response(serializer.data)
                else:
                    return Response({'detail': 'No data found for this city.'}, status=404)

        # If 'filter' is not 'latest', call the default behavior (which uses get_queryset)
        return super().list(request, *args, **kwargs)