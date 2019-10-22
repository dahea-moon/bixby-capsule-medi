import requests
import csv

# driver = webdriver.chrome()
f = open('수유실.csv', 'r', encoding='utf-8-sig')
reader = csv.DictReader(f)
i = 0
for row in reader:
    i += 1
    data = {}
    data['name'] = row.get('이름')
    data['address'] = row.get('주소')
    longt = float(row.get('경도'))
    data['longt'] = longt
    langt = float(row.get('위도'))
    data['langt'] = langt
    data['call'] = row.get('전화번호')
    print(i)
    r = requests.get('http://127.0.0.1:8000/api/sooyusil/collectdata/', data)
# response = driver.request('POST', 'U')