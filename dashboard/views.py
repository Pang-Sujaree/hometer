import json
import requests
from django.shortcuts import render
from django.http import JsonResponse,HttpRequest, HttpResponseRedirect
from django.urls import reverse
from .models import UserApi
from .forms import UserApiForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def thingspeak_api(request: HttpRequest):
    if request.method == 'POST':
        try:
            thingspeak_api = request.user.userapi 
            form = UserApiForm(request.POST, instance=thingspeak_api)
        except UserApi.DoesNotExist:
            form = UserApiForm(request.POST)
            thingspeak_api = None

        if form.is_valid():
            thingspeak_api = form.save(commit=False)
            thingspeak_api.user = request.user

            if thingspeak_api:
                thingspeak_api.save()
            else:
                thingspeak_api.save()

            return HttpResponseRedirect(reverse("dashboard"))
    else:
        try:
            thingspeak_api = request.user.userapi
            form = UserApiForm(instance=thingspeak_api)
        except UserApi.DoesNotExist:
            form = UserApiForm()
    return render(request, 'api.html', {'form': form})

@login_required
def dashboard(request):
   return render(request,'dashboard/dashboard.html')

def pzem_realtime_data(request,num_results=1):
    api = UserApi.objects.get(user=request.user)
    api_key = api.api_key
    channel_id = api.channel_id

    url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={api_key}&results={num_results}'

    response = requests.get(url)
    data = response.json()

    if 'feeds' in data:
        entries = data['feeds'][:num_results]

        pzem_data_list = []

        for entry in entries:
            pzem_data = {
                'timestamp': entry['created_at'],
                'voltage': entry['field1'],
                'current': entry['field2'],
                'power': entry['field3'],
                'energy': entry['field4'],
            }
            pzem_data_list.append(pzem_data)
    else:
        pzem_data_list = []
    return JsonResponse({'pzem_data_list': pzem_data_list})

def chart_view(request):
    data = pzem_realtime_data(request, num_results=10)
    return render(request, 'dashboard/index.html', {'pzem_data_list': data})