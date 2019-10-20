import requests
import csv


f = open('moonlight.csv', 'r', encoding='utf-8')
reader = csv.DictReader(f)
for row in reader:
    days = [('월', '1'), ('화', '2'), ('수', '3'), ('목', '4'), ('금', '5'), ('토', '6'), ('일', '7'), ('공', '8')]
    data = {}
    data['name'] = row.get('병원명')
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
            data['duty'+day[1]+'_open'] = row.get(day[0]+'open')
            data['duty'+day[1]+'_close'] = row.get(day[0]+'close')
    r = requests.get('http://127.0.0.1:8000/api/16/collectdata/', data)
