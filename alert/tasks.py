from celery import shared_task
from django.core.mail import send_mail
from .models import UserAlertConfig
from weather.models import WeatherData
def send_alert_email(rl):
    subject = 'Alert'
    message = 'Alert Alert Alert Alert Alert'
    html_message = '<p>Alert <strong>Temperature corresed Threshold</strong>!</p>'
    from_email = 'your_email@gmail.com'
    recipient_list = rl

    send_mail(subject, message, from_email, recipient_list, html_message=html_message)

@shared_task    
def send_alert():

    rl = []
    userAlerts = UserAlertConfig.objects.all()
    for user in userAlerts:
        weather = WeatherData.objects.filter(city=user.city).latest('timestamp')
        if weather.temp >= user.temp_threshold:
            rl.append(user.user_email)
    send_alert_email(rl)
   