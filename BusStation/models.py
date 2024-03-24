from django.contrib.auth.models import User
from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название станции")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Станция"
        verbose_name_plural = "Станции"

    pass


# автобусный рейс - Ries
class BusRoute(models.Model):
    number = models.IntegerField(verbose_name="Номер рейса")
    stations = models.ManyToManyField(Station)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = "Автобусный маршрут"
        verbose_name_plural = "Автобусные маршруты"

    pass


class Passenger(models.Model):
    passport = models.CharField(max_length=11, verbose_name="Данные паспорта")
    person = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.person.username

    class Meta:
        verbose_name = "Пассажир"
        verbose_name_plural = "Пассажиры"

    pass


class StationOfDeparture(models.Model):
    station = models.ForeignKey(Station, on_delete=models.PROTECT)
    bus_rout = models.ManyToManyField(BusRoute)

    def __str__(self):
        return self.station.name

    class Meta:
        verbose_name = "Станции отправления маршрута"
        verbose_name_plural = "Станции отправления маршрутов"

    pass


class StationOfArrived(models.Model):
    station = models.ForeignKey(Station, on_delete=models.PROTECT)
    bus_rout = models.ManyToManyField(BusRoute)

    def __str__(self):
        return self.station.name

    class Meta:
        verbose_name = "Станции прибытия маршрута"
        verbose_name_plural = "Станции прибытия маршрутов"

    pass


class RoutStations(models.Model):
    bus_rout = models.ForeignKey(BusRoute, on_delete=models.PROTECT)
    stations = models.ManyToManyField(Station)

    def __str__(self):
        return self.bus_rout.number

    class Meta:
        verbose_name = "Промежуточные станции маршрута"
        verbose_name_plural = "Промежуточные станции маршрутов"


class Ticket(models.Model):
    passenger = models.ManyToManyField(Passenger)
    date_of_departure = models.DateTimeField(verbose_name="Дата отправления")
    date_of_sell = models.DateTimeField(verbose_name="Дата покупки")
    station_of_departure = models.ManyToManyField(StationOfDeparture)
    station_of_arrived = models.ManyToManyField(StationOfArrived)
    seat = models.IntegerField(verbose_name="Посадочное место")

    def __str__(self):
        return str(self.id) + " " + str(self.passenger.person.username) \
               + str(self.station_of_departure) + "->" \
               + str(self.station_of_arrived) + str(self.date_of_departure)

    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"

    pass
