from django import forms
from django.forms import SelectDateWidget

from .widgets import AjaxInputWidget
from .models import City

CITIES = list((item['name'], item['name']) for item in City.objects.values('name').all() if item)


class SearchTicket(forms.Form):
    name_dep = forms.CharField(label="Город отрпавления",
                               widget=AjaxInputWidget(url='api/city_ajax', attrs={'class': 'inline right-margin'}))
    name_arr = forms.CharField(widget=forms.Select(choices=CITIES), label='Город прибытия')
    date = forms.DateField(widget=SelectDateWidget(), label='Дата')
