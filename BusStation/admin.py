from django.contrib import admin
from .models import *


admin.site.register(Ticket)
admin.site.register(Passenger)
admin.site.register(Station)
admin.site.register(BusRoute)
admin.site.register(StationOfArrived)
admin.site.register(StationOfDeparture)
admin.site.register(RoutStations)
admin.site.register(RaspisanieReisov)
