from django.urls import path, include
from . import views
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("signup", view=views.signup, name='signup'),
    path("wifi", view=views.wifi_info, name='wifi'),
    path('api/wifi_info/', view=views.get_wifi_info, name='get_wifi_info'),
]
