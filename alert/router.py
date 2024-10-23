from rest_framework.routers import SimpleRouter
from .views import UserAlertConfigViewSet

userAlertRouter = SimpleRouter()
userAlertRouter.register('user-alerts', UserAlertConfigViewSet)