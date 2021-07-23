from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome("./chromedriver")

name=[]
model=[]
price=[]
driven=[]
type=[]
gear=[]
city=[]

driver.get("https://www.cardekho.com/used-cars+10-lakh-to-5-crore+in+mumbai")

content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")

time.sleep(5)

for i in soup.find_all('div',attrs={'class': 'holder'}):
    p = i.find('span',attrs={'class': 'amnt'})
    n = i.find('a',title=True)
    m= i.find('div',attrs={'style': 'min-height: 16px; color: rgba(0, 0, 0, 0.6);'})
    d = i.find('span')

    if p != None and n['title'] != None and m != None and d != None:
        price.append(p.text)
        name.append(n['title'])
        model.append(m.text)
        driven.append(d.text)
    
for i in soup.find_all('div',attrs={'class': 'truncate dotlist'}):
    data = list(i.descendants)
    # print(i.find_next_sibling('span'))
    # print(i.find_next('span'))
    type.append(data[3])
    gear.append(data[5])

for i in soup.find_all('div',attrs={'class': 'cityIcon'}):
    data = list(i.descendants)
    if data[0] :
        city.append(data[1])
    else: 
        city.append('NA')

print(name)
print(price)
print(model)
print(driven)
print(type)
print(gear)
print(city)
print(len(name))
print(len(price))
print(len(model))
print(len(driven))
print(len(type))
print(len(gear))
print(len(city))

df = pd.DataFrame({'Car Name':name,'Model':model,'Driven (km)':driven,'Type':type,'Gear':gear,'Price':price}) 
df.to_csv('cars.csv', index=False, encoding='utf-8')
