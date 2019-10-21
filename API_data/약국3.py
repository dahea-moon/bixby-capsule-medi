import requests, csv
import xml.etree.ElementTree as ET

c = open('D:/BIxby/data/yg.csv', 'w', encoding='utf-8-sig')
cr = csv.writer(c)
cr.writerow(['주소', '이름', 'Tel', '월close', '월open', '화close', '화open', '수close', '수open', '목close', '목open', '금close', '금open', '토close', '토open', '일close', '일open', '공close', '공open', '위도', '경도'])
numbers = 1
while numbers < 2282:
    URL = f'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown?serviceKey=bEpUyM9O0kzJqUk4Bf7isM2hk8Z9olOG11SMihMDsgiB9sCmRThcLzX2eMThZYDMQ6k9R8g3RFbTXDLDqPm0qA%3D%3D&pageNo={numbers}&numOfRows=10'
    response = requests.get(URL).text
    f = open('D:/BIxby/data/response.xml', 'w', encoding='utf-8-sig')
    f.write(response)
    f.close()

    numbers += 1

    tree = ET.parse('response.xml')
    root = tree.getroot()
    
    for i in range(10):
        csv_input = []
        temp = []
        j = 0
        while True:
            try:
                xml_tag = root[1][0][i][j]
                if xml_tag.tag == 'dutyAddr':
                    csv_input += [xml_tag.text]
                    temp += [xml_tag.tag]
                if xml_tag.tag == 'dutyName':
                    csv_input += [xml_tag.text]
                    temp += [xml_tag.tag]
                if xml_tag.tag == 'dutyTel1':
                    csv_input += [xml_tag.text]
                    temp += [xml_tag.tag]
                for k in range(1, 9):
                    if xml_tag.tag == f'dutyTime{k}c':
                        csv_input += [xml_tag.text]
                        temp += [xml_tag.tag]
                    if xml_tag.tag == f'dutyTime{k}s':
                        csv_input += [xml_tag.text]
                        temp += [xml_tag.tag]
                if xml_tag.tag == 'wgs84Lon':
                    csv_input += [xml_tag.text]
                    temp += [xml_tag.tag]
                if xml_tag.tag == 'wgs84Lat':
                    csv_input += [xml_tag.text]
                    temp += [xml_tag.tag]
                j += 1
            except IndexError:
                break
        for l in range(1, 9):
            if f'dutyTime{l}c' not in temp:
                csv_input.insert(l*2+1, '')
            if f'dutyTime{l}s' not in temp:
                csv_input.insert(l*2+2, '')

        cr.writerow(csv_input)

c.close()


    