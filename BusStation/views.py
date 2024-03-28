from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .forms import currTicketForm, currTicketNoLoginForm
from .models import *


# Create your views here.
def Info(request):
    return render(request, 'pages/info.html')


def Profile(request):
    redirect('/')
    return render(request, 'pages/home.html')


class TicketCreate(CreateView):
    model = Ticket
    fields = '__all__'
    template_name = 'forms/form.html'


def getBusRoute(pk):
    return BusRoute.objects.get(id=pk)


@login_required
def buyCurrTicket(request, pk):
    bus_route = getBusRoute(pk)
    if request.method == "GET":
        form = currTicketForm()
        return render(request, 'forms/form.html', {'form': form})
    if request.method == 'POST':
        form = currTicketForm(request.POST)
        n_form = form.save(commit=False)
        n_form.date_of_sell = datetime.now()
        n_form.passenger = request.user.id
        n_form.save()

    pass


def buyCurrTicketNoLogin(request, pk):
    bus_route = getBusRoute(pk)
    if request.method == "GET":
        form = currTicketNoLoginForm()
        return render(request, 'forms/form.html', {'form': form})
    if request.method == 'POST':
        form = currTicketNoLoginForm(request.POST)
        if form.is_valid():
            n_form = form.save(commit=False)
            n_form.date_of_sell = datetime.now()
            n_form.save()

    pass