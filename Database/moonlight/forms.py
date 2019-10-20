from django import forms
from .models import Moonlight


class MoonlightModelForm(forms.ModelForm):
    class Meta:
        model = Moonlight
        fields = '__all__'
