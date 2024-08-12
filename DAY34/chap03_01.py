# 임의의 위키 페이지에서 모든 링크목록 가져오기
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html,'html.parser')
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

import re

body_content = bs.find('div',{'id':'bodyContent'})

pattern = '^(/wiki/)((?!:).)*$'
for link in body_content.find_all('a', href = re.compile(pattern)):
    print(link.attrs['href'])