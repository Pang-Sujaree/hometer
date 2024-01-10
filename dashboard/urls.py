from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', view=views.dashboard, name='dashboard'),

]