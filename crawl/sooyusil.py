from bs4 import BeautifulSoup
from selenium import webdriver
import csv

driver = webdriver.Chrome()
driver.get('https://sooyusil.com/?menuno=403')
for _ in range(362):
    driver.find_element_by_xpath('//*[@id="more"]').click()
    driver.implicitly_wait(2)

raw = driver.page_source
html = BeautifulSoup(raw, 'html.parser')
datalist = html.select('body > section.map_list.clearfix > ul > li > p')

f = open('sooyusil.csv', 'w', encoding='utf-8')
fieldnames = ['name', 'address', 'tel']
wr = csv.DictWriter(f, fieldnames=fieldnames)
wr.writeheader()

for data in datalist:
    name = data.strong.get_text()
    tel = data.a.get_text()
    address = data.strong.next_sibling.strip()
    wr.writerow({'name': name, 'tel': tel, 'address': address})
    