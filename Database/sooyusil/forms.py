from django import forms
from .models import Sooyusil


class SooyusilModelForm(forms.ModelForm):
    class Meta:
        model = Sooyusil
        fields = '__all__'