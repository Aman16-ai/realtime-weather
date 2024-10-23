from django.contrib import admin
from .models import UserAlertConfig,Alert
# Register your models here.
admin.site.register((UserAlertConfig,Alert))