from django import forms # type: ignore
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'brand','plate','name','createdby','like','photo']