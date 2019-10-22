from django import forms
from .models import Pharmacy


class PharmacyModelForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        fields = '__all__'
