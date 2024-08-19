from urllib.request import urlopen
from bs4 import BeautifulSoup

def parse_use_find(html):
    print('[find 함수 사용]')
    forecast_items = html.find_all('div',{'class':'tombstone-container'})
    print('총 tombstone-container 검색 개수 :',len(forecast_items))
    print('-'*50)
    for f in forecast_items:
        day = f.find('p',{'class':'period-name'})
        weather = f.find('p',{'class':'short-desc'})
        temp = f.find('p',{'class':'temp'})
        sub = f.find('img')['title']

        print(f'[Period]: {day.text}')
        print(f'[Short desc]: {weather.text}')
        print(f'[Temperature]: {temp.text}')
        print(f'[Image desc]: {sub}')
        print('-'*50)

def parse_use_select(html): 
    tombstone = html.select('div.tombstone-container')
    print('[select 함수 사용]')
    print(f'총 tombstone-container 검색 개수 :',len(tombstone))
    print('-'*50)
    for t in tombstone:
        day = t.select_one('.period-name')
        weather = t.select_one('.short-desc')
        temp = t.select_one('.temp')
        sub = t.select_one("img")['title']

        print(f'[Period]: {day.text}')
        print(f'[Short desc]: {weather.text}')
        print(f'[Temperature]: {temp.text}')
        print(f'[Image desc]: {sub}')
        print('-'*50)

def main():
    page = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Yst5ji9yxTY')
    html = BeautifulSoup(page.read(),'html.parser')

    print('National Weather Service Scraping')
    print('-'*50)

    parse_use_find(html)
    print('\n\n')
    parse_use_select(html)

main()