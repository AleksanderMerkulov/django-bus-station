from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # path('', views.Info, name='info'),
    # path('profile/', views.Profile, name='profile'),
    path('', views.Profile, name='profile'),
    path('change_info', views.change_profile, name='change_info'),
    path('route/<int:pk>', views.entry_bus_route, name='entry_bus_route'),
    path('comfort/<int:pk>', views.entry_comfort, name='entry_comfort'),
    path('ticket/<int:pk>', views.ticketRender, name='ticket_render'),
    path('buy/<int:pk>', views.buyCurrTicket),
    path('buy/<int:pk>/no_login', views.buyCurrTicketNoLogin),
    path('ticket_pdf', views.ticket_pdf),
    path('logs', views.showLog)

]
