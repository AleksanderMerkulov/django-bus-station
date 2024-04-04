from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # path('', views.Info, name='info'),
    # path('profile/', views.Profile, name='profile'),
    path('', views.Profile, name='profile'),
    path('change_info', views.change_profile, name='change_info'),
    # path('buy/', views.TicketCreate.as_view(), name='buy_ticket'),
    path('buy/<int:pk>', views.buyCurrTicket),
    path('buy/<int:pk>/no_login', views.buyCurrTicketNoLogin)

]
