import requests
import csv

# driver = webdriver.chrome()
f = open('수유실.csv', 'r', encoding='utf-8-sig')
reader = csv.DictReader(f)
for row in reader:
    data = {}
    data['name'] = row.get('이름')
    data['address'] = row.get('주소')
    data['longt'] = row.get('경도')
    data['langt'] = row.get('위도')
    data['call'] = row.get('전화번호')
    r = requests.get('http://127.0.0.1:8000/api/2/collectdata/', data)
# response = driver.request('POST', 'U')