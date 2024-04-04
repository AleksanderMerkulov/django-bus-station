from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView

from .forms import currTicketForm, currTicketNoLoginForm, changeInfoForm
from .models import *


# Create your views here.
def Info(request):
    return render(request, 'pages/info.html')


@login_required
def Profile(request):
    userID = request.user.id
    profile = Passenger.objects.filter(person_id=userID)
    if not profile:
        return redirect('/info/change_info')

    return render(request, 'pages/profile.html')

def create_profile(request):
    if request.method == "POST":
        pass

def change_profile(request):

    p = Passenger.objects.filter(person_id=request.user.id)

    if not p:
        if request.method == "GET":
            form = changeInfoForm()
            return render(request, 'forms/form.html', {'form': form})

        if request.method == "POST":
            form = changeInfoForm(request.POST)
            n_form = form.save(commit=False)
            n_form.person_id = request.user.id
            n_form.save()
            return redirect('/info/')
    else:
        person = Passenger.objects.get(person_id=request.user.id)
        if request.method == "GET":
            form = changeInfoForm(instance=person)
            return render(request, 'forms/form.html', {'form': form})

        if request.method == "POST":
            form = changeInfoForm(request.POST, instance=person)
            return redirect('/info/')

class TicketCreate(CreateView):
    model = Ticket
    fields = '__all__'
    template_name = 'forms/form.html'


def getBusRoute(pk):
    return BusRoute.objects.get(id=pk)


@login_required
def buyCurrTicket(request, pk):
    try:
        passanger = Passenger.objects.get(person_id=request.user.id)
    except ValueError:
        redirect('/profile/change')

    if request.method == "GET":
        form = currTicketForm()
        form.fields['route'].choices = RaspisanieReisov.objects.filter(bus_route__number=pk).values_list(
            'bus_route__number', 'date')
        return render(request, 'forms/form.html', {'form': form})
    if request.method == 'POST':
        form = currTicketForm(request.POST)
        n_form = form.save(commit=False)
        n_form.date_of_sell = datetime.now()
        n_form.passenger_id = request.user.id
        n_form.save()
        return redirect('/')
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
            n_form.seller_id = request.user.id
            n_form.save()
            return redirect('/')
    pass
