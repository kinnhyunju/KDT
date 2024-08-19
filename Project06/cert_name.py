from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import koreanize_matplotlib
import pandas as pd

import collections
if not hasattr(collections,'Callable'):
    collections.Callable = collections.abc.Callable

driver = webdriver.Chrome()

# 게시판 이름 받을 문자열
string = ''
for i in range(1,647):
    chrome_url = f'https://cafe.naver.com/sqlpd?iframe_url=/ArticleList.nhn%3Fsearch.clubid=21771779%26search.boardtype=L%26search.totalCount=1501%26search.cafeId=21771779%26search.page={i}'
    driver.get(chrome_url)

    driver.switch_to.frame("cafe_main")

    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')

    results = bs.find_all('a', {'class':'link_name'})
    
    for name in results:
        string = string + ' ' + name.text

print(string)

okt = Okt()
name_tag = okt.pos(string)

cate_list = []

for word, tag in name_tag:
    if word == 'Q':
        continue
    if word == 'A':
        continue
    if word == 'BooK':
        continue
    if word in ['분기']:
        cate_list.append('빅'+word)    
    if tag in ['Alpha']:
        cate_list.append(word)



counts = Counter(cate_list)
categories = counts.most_common(12)
dict_cate = dict(categories)

driver.quit()

print(dict_cate)

bull_name = list(dict_cate.keys())
bull_num = list(dict_cate.values())

cate_df = pd.DataFrame(zip(bull_name, bull_num))
cate_df.columns=['자격증 이름', '횟수']
cate_df.to_csv('certification.csv',index=False)