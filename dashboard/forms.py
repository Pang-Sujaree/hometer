from django import forms
from .models import UserApi

class UserApiForm(forms.ModelForm):
    class Meta:
        model = UserApi
        fields = ['api_key', 'channel_id']
