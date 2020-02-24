from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class CheckOutForm(forms.Form):
    street_address=forms.CharField()
    apartment_address=forms.CharField(required=False)
    country=CountryField(blank_label="--(Select Country)").formfield(
    widget=CountrySelectWidget()
    )
    zip=forms.CharField()
    payment_choices=(
    ('KCB','KCB'),
    ('M-Pesa','Mpesa'),
    ('Equity','Equity')
    )
    payment_option=forms.ChoiceField(widget=forms.RadioSelect(),choices=payment_choices)
