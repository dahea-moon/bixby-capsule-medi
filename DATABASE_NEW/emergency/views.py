from django.shortcuts import render
from .models import Emergency


def collectdata(request):
    if request.method == "GET":
        data = request.GET
        form = Emergency()
        form.name = data.get('name')
        form.address = data.get('address')
        form.place = data.get('place')
        form.longt = data.get('longt')
        form.langt = data.get('langt')
        form.call = data.get('call')
        if data.get('duty1') == 'False':
            form.duty1 = 'False'
        else:
            form.duty1 = 'True'
            form.duty1_open = data.get('duty1_open')
            if data.get('duty1_close') == '24:00:00':
                form.duty1_close = '23:59:59'
            else:
                form.duty1_close = data.get('duty1_close')
        if data.get('duty2') == 'False':
            form.duty2 = 'False'
        else:
            form.duty2 = 'True'
            form.duty2_open = data.get('duty2_open')
            if data.get('duty2_close') == '24:00:00':
                form.duty2_close = '23:59:59'
            else:
                form.duty2_close = data.get('duty2_close')
        if data.get('duty3') == 'False':
            form.duty3 = 'False'
        else:
            form.duty3 = 'True'
            form.duty3_open = data.get('duty3_open')
            if data.get('duty3_close') == '24:00:00':
                form.duty3_close = '23:59:59'
            else:
                form.duty3_close = data.get('duty3_close')
        if data.get('duty4') == 'False':
            form.duty4 = 'False'
        else:
            form.duty4 = 'True'
            form.duty4_open = data.get('duty4_open')
            if data.get('duty4_close') == '24:00:00':
                form.duty4_close = '23:59:59'
            else:
                form.duty4_close = data.get('duty4_close')
        if data.get('duty5') == 'False':
            form.duty5 = 'False'
        else:
            form.duty5 = 'True'
            form.duty5_open = data.get('duty5_open')
            if data.get('duty5_close') == '24:00:00':
                form.duty5_close = '23:59:59'
            else:
                form.duty5_close = data.get('duty5_close')
        if data.get('duty6') == 'False':
            form.duty6 = 'False'
        else:
            form.duty6 = 'True'
            form.duty6_open = data.get('duty6_open')
            if data.get('duty6_close') == '24:00:00':
                form.duty6_close = '23:59:59'
            else:
                form.duty6_close = data.get('duty6_close')
        if data.get('duty7') == 'False':
            form.duty7 = 'False'
        else:
            form.duty7 = 'True'
            form.duty7_open = data.get('duty7_open')
            if data.get('duty7_close') == '24:00:00':
                form.duty7_close = '23:59:59'
            else:
                form.duty7_close = data.get('duty7_close')
        if data.get('duty8') == 'False':
            form.duty8 = 'False'
        else:
            form.duty8 = 'True'
            form.duty8_open = data.get('duty8_open')
            if data.get('duty8_close') == '24:00:00':
                form.duty8_close = '23:59:59'
            else:
                form.duty8_close = data.get('duty8_close')
        form.save()
