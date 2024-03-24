from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from BusStation.models import BusRoute


def HomePage(request):
    routes = BusRoute.objects.all()
    return render(request, 'pages/home.html', {'routes': routes})
    pass


def redirectToProfile(request):
    return redirect('profile')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    redirect_field_name = "home"
