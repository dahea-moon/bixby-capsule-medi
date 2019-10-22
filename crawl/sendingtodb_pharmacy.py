import requests
import csv


f = open('yg.csv', 'r', encoding='utf-8-sig')
reader = csv.DictReader(f)
for row in reader:
    days = [('월', '1'), ('화', '2'), ('수', '3'), ('목', '4'), ('금', '5'), ('토', '6'), ('일', '7'), ('공', '8')]
    data = {}
    data['name'] = row.get('이름')
    data['address'] = row.get('주소')
    data['longt'] = row.get('경도')
    data['langt'] = row.get('위도')
    data['call'] = row.get('Tel')
    for day in days:
        if row.get(day[0]+'open') == '':
            data['duty'+day[1]] = 'False'
            data['duty'+day[1]+'_open'] = 'None'
            data['duty'+day[1]+'_close'] = 'None'
        else:
            data['duty'+day[1]] = 'True'
            opentime = row.get(day[0]+'open')
            opentime = opentime[:-2] + ':' + opentime[-2:]
            data['duty'+day[1]+'_open'] = opentime
            closetime = row.get(day[0]+'close')
            closetime = closetime[:-2] + ':' + closetime[-2:]
            data['duty'+day[1]+'_close'] = closetime
    r = requests.get('http://127.0.0.1:8000/api/3/collectdata/', data)
