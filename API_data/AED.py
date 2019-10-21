import requests, csv
import xml.etree.ElementTree as ET

c = open('D:/BIxby/data/data_3/AED.csv', 'w', encoding='utf-8-sig')
cr = csv.writer(c)
cr.writerow(['주소', '간이약도', '관리자', 'Tel', '위도lon', '경도lat'])
numbers = 1
while numbers < 1702:
    URL = f'http://apis.data.go.kr/B552657/AEDInfoInqireService/getAedFullDown?serviceKey=bEpUyM9O0kzJqUk4Bf7isM2hk8Z9olOG11SMihMDsgiB9sCmRThcLzX2eMThZYDMQ6k9R8g3RFbTXDLDqPm0qA%3D%3D&pageNo={numbers}&numOfRows=10'
    response = requests.get(URL).text
    f = open('D:/BIxby/data/data_3/AED_response.xml', 'w', encoding='utf-8-sig')
    f.write(response)
    f.close()

    numbers += 1

    tree = ET.parse('D:/BIxby/data/data_3/AED_response.xml')
    root = tree.getroot()
    
    for i in range(10):
        csv_input = []
        temp = []
        j = 0
        while True:
            try:
                xml_tag = root[1][0][i][j]
                if xml_tag.tag == 'buildAddress':
                    csv_input += [xml_tag.text]
                    temp += [xml_tag.tag]
                if xml_tag.tag == 'buildPlace':
                    csv_input += [xml_tag.text]
                    temp += [xml_tag.tag]
                if xml_tag.tag == 'manager':
                    csv_input += [xml_tag.text]
                    temp += [xml_tag.tag]
                if xml_tag.tag == 'managerTel':
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

        if 'buildPlace' not in temp:
            csv_input.insert(1, '')
        if 'manager' not in temp:
            csv_input.insert(2, '')
        if 'managerTel' not in temp:
            csv_input.insert(3, '')


        cr.writerow(csv_input)

c.close()


    