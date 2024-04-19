from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.admin.models import LogEntry
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table

from .forms import currTicketForm, currTicketNoLoginForm, changeInfoForm
from .models import *

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet


# Create your views here.
def Info(request):
    return render(request, 'pages/info.html')


@login_required
def Profile(request):
    userID = request.user.id
    profile = Passenger.objects.get(person_id=userID)
    if not profile:
        return redirect('/info/change_info')
    tickets = Ticket.objects.filter(passenger_id=userID)
    return render(request, 'pages/profile.html', {
        'tickets': tickets,
        'profile': profile
    })


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
            exists = Passenger.objects.filter(passport=n_form.passport).exists()
            if exists:
                return render(request, 'forms/form.html', {'form': form, 'err': 'Такие паспортные данные существуют'})
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
    passanger = None
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
        busRoute = BusRoute.objects.get(number=pk)
        rest_of_money = passanger.balance - busRoute.cost
        if rest_of_money < 0:
            form.fields['route'].choices = RaspisanieReisov.objects.filter(bus_route__number=pk).values_list(
                'bus_route__number', 'date')
            return render(request, 'forms/form.html', {'form': form, 'err': 'Недостаточно денег!'})
        passanger.balance = rest_of_money
        n_form.save()
        passanger.save()
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


def showLog(request):
    if request.user.is_superuser:
        logs = LogEntry.objects.all()
        return render(request, "pages/logs.html", {'logs': logs})
    else:
        return render(request, 'pages/not_allowed.html')

def ticket_pdf(request):
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    ticket = Ticket.objects.all()
    ticket_no_login = TicketNoLogin.objects.all()

    # Настройка PDF
    pdf_filename = "output.pdf"
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Определение стилей
    styles = getSampleStyleSheet()
    styleH = styles["Heading1"]

    # Форматирование данных в виде списка списков для таблицы
    table_data = [['Number', 'Passenger', 'Date of sell']]  # заголовки таблицы
    for entry in ticket:
        table_data.append([entry.id, entry.passenger, entry.date_of_sell])  # добавление данных из модели
    for entry in ticket_no_login:
        table_data.append([entry.id, entry.passengerFIO, entry.date_of_sell])  # добавление данных из модели

    # Создание таблицы с данными
    table = Table(table_data, repeatRows=1)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ]))

    # Добавление таблицы в элементы PDF
    elements.append(table)

    # Генерация PDF
    doc.build(elements)

    # Сброс указателя потока обратно в начало
    buffer.seek(0)

    # Создание FileResponse
    response = FileResponse(buffer, as_attachment=True, filename='output.pdf')

    return response


def ticketRender(request, pk):
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    ticket = Ticket.objects.get(id=pk)

    # Настройка PDF
    pdf_filename = "output.pdf"
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Определение стилей
    styles = getSampleStyleSheet()
    styleH = styles["Heading1"]

    # Форматирование данных в виде списка списков для таблицы
    table_data = [['Number', 'Passenger', 'Date of sell']]  # заголовки таблицы
    table_data.append([ticket.id, ticket.passenger, ticket.date_of_sell])  # добавление данных из модели


    # Создание таблицы с данными
    table = Table(table_data, repeatRows=1)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.white),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                               ]))

    # Добавление таблицы в элементы PDF
    elements.append(table)

    # Генерация PDF
    doc.build(elements)

    # Сброс указателя потока обратно в начало
    buffer.seek(0)

    # Создание FileResponse
    response = FileResponse(buffer, as_attachment=True, filename='output.pdf')

    return response


def entry_bus_route(request, pk):
    bus_route_entry = BusRoute.objects.get(number=pk)

    return render(request, 'pages/entry.html', {'route': bus_route_entry})


def entry_comfort(request, pk):
    comfort_entry = Comfort.objects.get(id=pk)

    return render(request, 'pages/comfort_entry.html', {'comfort': comfort_entry})
