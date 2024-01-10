# models.py
from django.db import models
from django.contrib.auth.models import User

class UserApi(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=50)
    channel_id = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class ThingSpeakData(models.Model):
    voltage = models.FloatField()
    current = models.FloatField()
    power = models.FloatField()
    energy = models.FloatField()
    created_at = models.DateTimeField()
    
    def __str__(self):
        return f'ThingSpeakData at {self.created_at}'
