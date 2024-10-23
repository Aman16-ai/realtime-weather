from django.contrib import admin
from django.urls import path,include
from .router import dailyWeatherSummaryRouter,weatherRouter
urlpatterns = [
    path('summary/', include(dailyWeatherSummaryRouter.urls)),
    path('',include(weatherRouter.urls))
]
