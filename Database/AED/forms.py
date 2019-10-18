from django import forms
from .models import AED


class AEDModelForm(forms.ModelForm):
    name = forms.CharField(min_length=2, max_length=200)
    address = forms.CharField(min_length=10, max_length=200)
    longt = forms.FloatField()
    langt = forms.FloatField()
    call = forms.CharField(min_length=3, max_length=100)

    class Meta:
        model = AED
        fields = '__all__'