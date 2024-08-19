import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import collections

if not hasattr(collections,'Callable'):
    collections.Callable = collections.abc.Callable

html = requests.get('https://finance.naver.com/sise/sise_market_sum.naver')
soup = BeautifulSoup(html.text, 'html.parser')
kospi = soup.find_all('a',{'class':'tltle'})

# 정보 담아올 리스트
name_list = []
code_list = []
url_list = []

# 기업 이름 가져오기
for t in kospi[:10]:
    name_list.append(t.text)
# 기업 코드 가져오기
for link in kospi[:10]:
    if 'href' in link.attrs:
        code_list.append(link.attrs['href'])
# 주식 정보 링크 만들기
for i in range(len(code_list)):
    base_url = 'https://finance.naver.com/'
    company_url = f'{code_list[i]}'
    sum_url = base_url + company_url
    url_list.append(sum_url)

# 주가 정보 가져오기
def get_info(num):
    link = requests.get(url_list[num-1])
    bs = BeautifulSoup(link.text, 'html.parser')
    stock_info = bs.find('dl',{'class':'blind'})
    stock = stock_info.find_all('dd')
    name = stock[1].text.split()[1]
    code = stock[2].text.split()[1]
    cost = stock[3].text.split()[1]
    yesterday= stock[4].text.split()[1]
    now = stock[5].text.split()[1]
    high = stock[6].text.split()[1]
    low = stock[8].text.split()[1]

    print(f'종목명: {name}')
    print(f'종목코드: {code}')
    print(f'현재가: {cost}')
    print(f'전일가: {yesterday}')
    print(f'시가: {now}')
    print(f'고가: {high}')
    print(f'저가: {low}')

# 메뉴 출력
def menu():
    print('-'*25)
    print('[ 네이버 코스피 상위 10대 기업 목록 ]')
    print('-'*25)
    for i in range(len(name_list)):
        print(f'[{i+1:2}] {name_list[i]}')

def main():
    while True:
        menu()
        number = int(input('주가를 검색할 기업의 번호를 입력하세요 (-1: 종료) : '))
        if number == -1: 
            print('프로그램 종료')
            break
        elif number>=1 and number<=10:
            print(url_list[number-1])
            get_info(number)
        else:
            print('올바른 숫자가 아닙니다. 1~10까지의 숫자를 입력하세요.')

main()