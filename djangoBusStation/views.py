from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.db.models import Q

from BusStation.models import BusRoute, Station, Comfort


def HomePage(request):
    stations = Station.objects.all()
    comforts = Comfort.objects.all()

    comfort = request.GET.getlist('comfort')
    for i, tag in enumerate(comfort):
        comfort[i] = int(tag)
    toilet = request.GET.get('toilet')
    aircool = request.GET.get('aircool')
    depart = request.GET.getlist('depart')
    for i, tag in enumerate(depart):
        depart[i] = int(tag)
    arrived = request.GET.getlist('arrived')
    for i, tag in enumerate(arrived):
        arrived[i] = int(tag)
    routes = BusRoute.objects.all()
    if comfort:
        routes = routes.filter(comfort__in=comfort)
    if toilet:
        routes = routes.filter(toilet=bool(toilet))
    if aircool:
        routes = routes.filter(aircool=bool(aircool))
    if depart:
        routes = routes.filter(depart_station_id__in=depart)
    if arrived:
        routes = routes.filter(Q(arr_station_id__in=arrived) | Q(stations__in=arrived))

    content = {
        'routes': routes,
        'stations': stations,
        'comform': comfort,
        'comforts': comforts,
        'toilet': toilet,
        'aircool': aircool,
        'depart': depart,
        'arrived': arrived,

    }

    return render(request, 'pages/home.html', content)
    pass


def redirectToProfile(request):
    return redirect('profile')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    redirect_field_name = "home"
