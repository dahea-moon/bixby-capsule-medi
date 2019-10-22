from django.shortcuts import render
from .models import AED

def collectdata(request):
    if request.method == "GET":
        data = request.GET
        form = AED()
        form.name = data.get('name')
        form.address = data.get('address')
        form.longt = data.get('longt')
        form.langt = data.get('langt')
        form.call = data.get('call')
        form.save()