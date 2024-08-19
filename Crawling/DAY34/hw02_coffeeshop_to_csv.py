from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate


loc_list = []
name_list = []
address_list = []
tel_number_list = []

# 1~49 페이지 데이터 추가
for n in range(1,50):
    html = urlopen(f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={n}&sido=&gugun=&store=')
    coffee_bs = BeautifulSoup(html,'html.parser')
    coffe_tag = coffee_bs.find_all('td')

    for i in range(10):
        loc = coffe_tag[6*i].text
        name = coffe_tag[6*i+1].text
        address = coffe_tag[6*i+3].text
        tel_number = coffe_tag[6*i+5].text

        loc_list.append(loc)
        name_list.append(name)
        address_list.append(address)
        tel_number_list.append(tel_number)

# 50페이지 데이터 추가
html = urlopen(f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=50&sido=&gugun=&store=')
coffee_bs = BeautifulSoup(html,'html.parser')
coffe_tag = coffee_bs.find_all('td')

for i in range(5):
    loc = coffe_tag[6*i].text
    name = coffe_tag[6*i+1].text
    address = coffe_tag[6*i+3].text
    tel_number = coffe_tag[6*i+5].text

    loc_list.append(loc)
    name_list.append(name)
    address_list.append(address)
    tel_number_list.append(tel_number)

coffee_df = pd.DataFrame({'매장이름':name_list,'지역':loc_list,'주소':address_list,'전화번호':tel_number_list})


for i in range(len(coffee_df)):
    print(f"[{i+1:3}]: 매장이름: {coffee_df.loc[i,'매장이름']}, 지역: {coffee_df.loc[i,'지역']}, 주소: {coffee_df.loc[i,'주소']}, 전화번호: {coffee_df.loc[i,'전화번호']}")
print('전체 매장 수:', len(coffee_df))
coffee_df.to_csv('hollys_branches.csv',index=False, encoding='utf-8')
print('hollys_branches.csv 파일 저장 완료')