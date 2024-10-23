from rest_framework.routers import SimpleRouter
from .views import DailyWeatherSummaryViewset,WeatherViewset
dailyWeatherSummaryRouter = SimpleRouter()

dailyWeatherSummaryRouter.register("",DailyWeatherSummaryViewset)

weatherRouter = SimpleRouter()
weatherRouter.register("",WeatherViewset)