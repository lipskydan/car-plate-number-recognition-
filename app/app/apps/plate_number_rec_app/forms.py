from django import forms
from django.forms import widgets

from .models import CarPlateNumber


class CarPlateNumberForm(forms.ModelForm):
    class Meta:
        model = CarPlateNumber
        fields = ('car_plate_img',)
        widgets = {'car_plate_img': forms.FileInput(
            attrs={'style': 'display: none;', 'class': 'form-control', 'required': False, }
        )}
