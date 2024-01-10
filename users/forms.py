from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import WiFiInfo

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class WiFiInfoForm(forms.ModelForm):
    class Meta:
        model = WiFiInfo
        fields = ['wifi_ssid', 'wifi_password']
        labels = {
            'wifi_ssid': 'ชื่อเครื่อข่าย WiFi',
            'wifi_password': 'รหัสผ่าน WiFi'
        }