from django import forms
from django.forms.extras.widgets import SelectDateWidget

from .models import Reservation

import datetime


# form for restaurant reservation
class ReservationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128, required=True, \
                                 widget=forms.TextInput(attrs={'required': 'true'}), \
                                 help_text="First name")
    last_name = forms.CharField(max_length=128, required=True,
                                widget=forms.TextInput(attrs={'required': 'true'}),\
                                help_text="Last name")
    city = forms.CharField(max_length=128, required=True, help_text="City")
    reservation_date = forms.DateField(help_text="Reservation date", \
                                       widget=SelectDateWidget(attrs={'required': 'true'}))
    phone_number = forms.CharField(max_length=128, required=True, \
                                   widget=forms.TextInput(attrs={'required': 'true'}), \
                                   help_text="Phone number")
    email = forms.EmailField(max_length=128, help_text="Email")
    comment = forms.CharField(max_length=200, widget=forms.Textarea)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Reservation
        fields = ('first_name','last_name', 'city', 'reservation_date', 'phone_number', 'email', 'comment')

