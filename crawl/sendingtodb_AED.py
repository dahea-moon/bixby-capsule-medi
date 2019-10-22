import requests
import csv

# driver = webdriver.chrome()
f = open('AED.csv', 'r', encoding='utf-8-sig')
reader = csv.DictReader(f)
for row in reader:
    data = {}
    data['address'] = row.get('주소')
    data['place'] = row.get('간이약도')
    data['manager'] = row.get('관리자')
    data['longt'] = row.get('경도lat')
    data['langt'] = row.get('위도lon')
    data['call'] = row.get('Tel')
    r = requests.get('http://127.0.0.1:8000/api/AED/collectdata/', data)
