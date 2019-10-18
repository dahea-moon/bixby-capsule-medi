from django import forms
from .models import Moonlight


class MoonlightModelForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200)
    place = forms.CharField(max_length=100, null=True, blank=True)
    longt = forms.FloatField()
    langt = forms.FloatField()
    call = forms.CharField(max_length=100)
    duty1 = forms.BooleanField()
    duty2 = forms.BooleanField()
    duty3 = forms.BooleanField()
    duty4 = forms.BooleanField()
    duty5 = forms.BooleanField()
    duty6 = forms.BooleanField()
    duty7 = forms.BooleanField()
    duty8 = forms.BooleanField()
    duty1_open = forms.TimeField(null=True, blank=True)
    duty1_close = forms.TimeField(null=True, blank=True)
    duty2_open = forms.TimeField(null=True, blank=True)
    duty2_close = forms.TimeField(null=True, blank=True)
    duty3_open = forms.TimeField(null=True, blank=True)
    duty3_close = forms.TimeField(null=True, blank=True)
    duty4_open = forms.TimeField(null=True, blank=True)
    duty4_close = forms.TimeField(null=True, blank=True)
    duty5_open = forms.TimeField(null=True, blank=True)
    duty5_close = forms.TimeField(null=True, blank=True)
    duty6_open = forms.TimeField(null=True, blank=True)
    duty6_close = forms.TimeField(null=True, blank=True)
    duty7_open = forms.TimeField(null=True, blank=True)
    duty7_close = forms.TimeField(null=True, blank=True)
    duty8_open = forms.TimeField(null=True, blank=True)
    duty8_close = forms.TimeField(null=True, blank=True)

    class Meta:
        model = Moonlight
        fields = '__all__'
