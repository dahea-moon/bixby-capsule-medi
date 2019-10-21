import json, requests, csv
from bs4 import BeautifulSoup


# print(soup)

# jsonObject = json.loads(str(soup))
# data = jsonObject['item']
 
# for item in data:
#     result = "{}".format(item['dutyaddr'])
#     print(result)



with open('test2.csv','w', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    number = 1
    while number < 7105:
        URL = f'http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncFullDown?serviceKey=bEpUyM9O0kzJqUk4Bf7isM2hk8Z9olOG11SMihMDsgiB9sCmRThcLzX2eMThZYDMQ6k9R8g3RFbTXDLDqPm0qA%3D%3D&pageNo={number}&numOfRows=10'
        response = requests.get(URL).text

        soup = BeautifulSoup(response, 'html.parser').select('item')
        w.writerows(soup)

        number += 1