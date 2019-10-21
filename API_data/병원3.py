import requests
f = open('hos_test.xml','w', encoding='utf-8-sig')

number = 1
URL = f'http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncFullDown?serviceKey=bEpUyM9O0kzJqUk4Bf7isM2hk8Z9olOG11SMihMDsgiB9sCmRThcLzX2eMThZYDMQ6k9R8g3RFbTXDLDqPm0qA%3D%3D&pageNo={number}&numOfRows=10'
response = requests.get(URL).text

f.write(response)

f.close()
