from django.http import HttpRequest, HttpResponseRedirect, JsonResponse
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404
from users.forms import SignUpForm, WiFiInfoForm
from django.urls import reverse
from .models import WiFiInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def signup(request: HttpRequest):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
    else:
        form = SignUpForm()

    context = {"form": form}
    return render(request, 'signup.html', context)

def wifi_info(request: HttpRequest):
    if request.method == 'POST':
        try:
            wifi_info = request.user.wifiinfo 
            form = WiFiInfoForm(request.POST, instance=wifi_info)
        except WiFiInfo.DoesNotExist:
            form = WiFiInfoForm(request.POST)
            wifi_info = None

        if form.is_valid():
            wifi_info = form.save(commit=False)
            wifi_info.user = request.user

            if wifi_info:
                wifi_info.save()
            else:
                wifi_info.save()

            return HttpResponseRedirect(reverse("home"))
    else:
        try:
            wifi_info = request.user.wifiinfo
            form = WiFiInfoForm(instance=wifi_info)
        except WiFiInfo.DoesNotExist:
            form = WiFiInfoForm()

    return render(request, 'wifi_setup.html', {'form': form})

def get_wifi_info(request):
    if request.method == 'GET':
        wifi_info = {
            'wifi_ssid': getattr(request.user.wifiinfo, 'wifi_ssid', 'default_ssid'),
            'wifi_password': getattr(request.user.wifiinfo, 'wifi_password', 'default_password'),
        }
        return JsonResponse(wifi_info)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)