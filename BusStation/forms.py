from django import forms

from BusStation.models import Ticket, TicketNoLogin, RaspisanieReisov, Passenger


class changeInfoForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = '__all__'
        # exclude = ['person']


class currTicketForm(forms.ModelForm):
    #
    # def __init__(self, *args, pk=None, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['route'].widget.attrs.update({'class': f'{pk}'})
    #     pass

    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['passenger', 'date_of_sell']
        # exclude = [ 'date_of_sell']
    pass


class currTicketNoLoginForm(forms.ModelForm):
    class Meta:
        model = TicketNoLogin
        fields = '__all__'
        exclude = ['date_of_sell', 'seller']
    pass