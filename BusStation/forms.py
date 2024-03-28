from django import forms

from BusStation.models import Ticket, TicketNoLogin


class currTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['passenger', 'date_of_sell']
    pass


class currTicketNoLoginForm(forms.ModelForm):
    class Meta:
        model = TicketNoLogin
        fields = '__all__'
        exclude = ['date_of_sell']
    pass