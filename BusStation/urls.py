from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Info, name='info'),
    path('profile/', views.Profile, name='profile'),
    path('buy/', views.TicketCreate.as_view(), name='buy_ticket'),

]
