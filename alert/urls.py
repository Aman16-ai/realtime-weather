from django.urls import path, include
from .router import userAlertRouter
urlpatterns = [
    path('', include(userAlertRouter.urls)),  # Include the generated URLs in the urlpatterns
]