from django.shortcuts import render, redirect
from django.views.generic import CreateView
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
