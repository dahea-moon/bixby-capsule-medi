from django import forms
from .models import AED


class AEDModelForm(forms.ModelForm):
    class Meta:
        model = AED
        fields = '__all__'