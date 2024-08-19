from bs4 import BeautifulSoup
from selenium import webdriver

from konlpy.tag import Hannanum
from collections import Counter
import matplotlib.pyplot as plt
import koreanize_matplotlib
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import time

import platform

from urllib.request import Request

import collections
if not hasattr(collections,'Callable'):
    collections.Callable = collections.abc.Callable

driver = webdriver.Chrome()


# 게시글 번호 받을 리스트
num_list = []

# SQLD -----------------------------------------------------------------------------------------------------------
for i in range(1,5):
    chrome_url=f"https://cafe.naver.com/sqlpd?iframe_url=/ArticleSearchList.nhn%3Fsearch.clubid=21771779%26search.menuid=145%26search.media=0%26search.searchdate=all%26search.defaultValue=1%26userDisplay=50%26search.option=0%26search.sortBy=date%26search.searchBy=0%26search.query=%C7%D5%B0%DD%26search.viewtype=title%26search.page={i}"
    driver.get(chrome_url)
    time.sleep(1)

    driver.switch_to.frame("cafe_main")

    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')

    results = bs.find_all('div', {'class':'inner_number'})

    for num in results:
        num_list.append(int(num.text))
print(num_list)

# 게시글 내용 문자열로 합치기
string = ''
word_list = []
for n in num_list:
    url = f"https://cafe.naver.com/sqlpd?iframe_url_utf8=%2FArticleRead.nhn%253Fclubid%3D21771779%2526page%3D1%2526menuid%3D132%2526inCafeSearch%3Dtrue%2526searchBy%3D1%2526query%3D%25ED%2595%25A9%25EA%25B2%25A9%2526includeAll%3D%2526exclude%3D%2526include%3D%2526exact%3D%2526searchdate%3Dall%2526media%3D0%2526sortBy%3Ddate%2526articleid%3D{n}%2526referrerAllArticles%3Dfalse"
    driver.get(url)
    time.sleep(1.5)

    driver.switch_to.frame("cafe_main")

    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')

    results = bs.find_all('div', {"class" : "se-module"})
    for str in results:
        word_list.append(str.text)

driver.quit()
string = ''.join(word_list)

print(string)

hnn = Hannanum()
name_tag = hnn.pos(string)

word_list = []
for msg, tag in name_tag:
    if tag in ['N']:
        if len(msg) > 5:
            continue
        if msg.find('주') >= 0:
            word_list.append(msg)
        
        if msg.find('일') >= 0:
            word_list.append(msg)
        
        if msg.find('시간') >= 0:
            word_list.append(msg)

        if msg.find('점') >= 0:
            word_list.append(msg)
        

counts = Counter(word_list)
words = counts.most_common(50)
words_dict = dict(words)

del_words = ['점수', '시간', '일', '주' '위주', '고득점', '사전점수', '\u200b일단', '\u200b점심시간', '화요일', '주말', '주문', '다음주']

for word in del_words:
    if word in words_dict:
        words_dict.pop(word)

print(words_dict)


# 한글을 분석하기 위해 font를 한글로 지정, macOS는 .otf, windows 는 .ttf 파일의 위치를 지정
if platform.system() == 'Windows':
    path = r'C:\Users\kdp\AppData\Local\Microsoft\Windows\Fonts\NanumBarunpenR.ttf'

img_mask = np.array(Image.open('book.jpg'))
wc = WordCloud(font_path=path, width=400, height=400, background_color='white',
               max_font_size=200, repeat=True, colormap='gist_earth', mask=img_mask)
cloud = wc.generate_from_frequencies(words_dict)

# 생성된 Wordcloud를 test.jpg로 보낸다,
# cloud.to_file('test.jpg')
plt.figure(figsize=(10,8))
plt.axis('off')
plt.imshow(cloud)
plt.title('SQLD 합격 후기 본문 형태소 분석')
plt.show()

# ADsP -------------------------------------------------------------------------------------------------------

for i in range(1,5):
    chrome_url=f"https://cafe.naver.com/sqlpd?iframe_url=/ArticleSearchList.nhn%3Fsearch.clubid=21771779%26search.menuid=132%26search.media=0%26search.searchdate=all%26search.defaultValue=1%26userDisplay=50%26search.option=0%26search.sortBy=date%26search.searchBy=0%26search.query=%C7%D5%B0%DD%26search.viewtype=title%26search.page={i}"
    driver.get(chrome_url)
    time.sleep(1)

    driver.switch_to.frame("cafe_main")

    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')

    results = bs.find_all('div', {'class':'inner_number'})

    for num in results:
        num_list.append(int(num.text))
print(num_list)

string = ''
word_list = []
for n in num_list:
    url = f"https://cafe.naver.com/sqlpd?iframe_url_utf8=%2FArticleRead.nhn%253Fclubid%3D21771779%2526page%3D1%2526menuid%3D132%2526inCafeSearch%3Dtrue%2526searchBy%3D1%2526query%3D%25ED%2595%25A9%25EA%25B2%25A9%2526includeAll%3D%2526exclude%3D%2526include%3D%2526exact%3D%2526searchdate%3Dall%2526media%3D0%2526sortBy%3Ddate%2526articleid%3D{n}%2526referrerAllArticles%3Dfalse"
    driver.get(url)
    time.sleep(1.5)

    driver.switch_to.frame("cafe_main")

    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')

    results = bs.find_all('div', {"class" : "se-module"})
    for str in results:
        word_list.append(str.text)

driver.quit()
string = ''.join(word_list)

print(string)

hnn = Hannanum()
name_tag = hnn.pos(string)

word_list = []
for msg, tag in name_tag:
    if tag in ['N']:
        if len(msg) > 5:
            continue
        if msg.find('주') >= 0:
            word_list.append(msg)
        
        if msg.find('일') >= 0:
            word_list.append(msg)
        
        if msg.find('시간') >= 0:
            word_list.append(msg)

        if msg.find('점') >= 0:
            word_list.append(msg)
        

counts = Counter(word_list)
words = counts.most_common(50)
words_dict = dict(words)

del_words = ['시간', '점수', '일', '주', '주관식', '고득점', '가채점', '주말', '시간이', '파일' ,'이점', '사전점수']

for word in del_words:
    if word in words_dict:
        words_dict.pop(word)

print(words_dict)


# 한글을 분석하기 위해 font를 한글로 지정, macOS는 .otf, windows 는 .ttf 파일의 위치를 지정
if platform.system() == 'Windows':
    path = r'C:\Users\kdp\AppData\Local\Microsoft\Windows\Fonts\NanumBarunpenR.ttf'

img_mask = np.array(Image.open('book.jpg'))
wc = WordCloud(font_path=path, width=400, height=400, background_color='white',
               max_font_size=200, repeat=True, colormap='inferno', mask=img_mask)
cloud = wc.generate_from_frequencies(words_dict)

# 생성된 Wordcloud를 test.jpg로 보낸다,
# cloud.to_file('test.jpg')
plt.figure(figsize=(10,8))
plt.axis('off')
plt.imshow(cloud)
plt.title('ADsP 합격 후기 본문 형태소 분석')
plt.show()