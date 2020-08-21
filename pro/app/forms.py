from django import forms
from .models import employee

class employeeForm(forms.Form):
    name = forms.CharField(required=False)
    company = forms.CharField(required=False)
    salary= forms.CharField(required=False)
    #holiday_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))

class allupdate(forms.Form):
    column_to_update=forms.CharField(required=True)
    new_value=forms.CharField(required=True)



