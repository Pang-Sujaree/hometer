from django.db import models
from django.contrib.auth.models import User

class WiFiInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wifi_ssid = models.CharField(max_length=50)
    wifi_password = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
