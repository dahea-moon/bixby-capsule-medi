import requests
import csv

f = open('AED.csv', 'r', encoding='utf-8-sig')
reader = csv.DictReader(f)
i = 0
for row in reader:
    i += 1
    data = {}
    data['address'] = row.get('주소')
    data['place'] = row.get('간이약도')
    data['manager'] = row.get('관리자')
    longt = float(row.get('경도lat'))
    data['longt'] = longt
    langt = float(row.get('위도lon'))
    data['langt'] = langt
    data['call'] = row.get('Tel')
    print(i)
    r = requests.get('http://127.0.0.1:8000/api/AED/collectdata/', data)
