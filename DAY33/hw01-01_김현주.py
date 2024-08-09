from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Yst5ji9yxTY')
bs = BeautifulSoup(html.read(),'html.parser')
tombstone = bs.select('div.tombstone-container')

for t in tombstone:
    day = t.select_one('.period-name')
    weather = t.select_one('.short-desc')
    temp = t.select_one('.temp')
    sub = t.select_one("img")['title']

    print(f'[Period]: {day.text}')
    print(f'[Short desc]: {weather.text}')
    print(f'[Temperature]: {temp.text}')
    print(f'[Image desc]: {sub}')
    print('-'*40)