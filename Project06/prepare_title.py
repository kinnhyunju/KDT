from bs4 import BeautifulSoup
from selenium import webdriver

from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import koreanize_matplotlib

from wordcloud import WordCloud
import numpy as np
from PIL import Image

from konlpy.tag import Hannanum

import platform

import collections
if not hasattr(collections,'Callable'):
    collections.Callable = collections.abc.Callable

driver = webdriver.Chrome()

# SQLD 게시글 제목 받기 -----------------------------------------------------------------------------
word_list = []
for i in range(1,10):
    chrome_url=f"https://cafe.naver.com/sqlpd?iframe_url=/ArticleSearchList.nhn%3Fsearch.clubid=21771779%26search.menuid=145%26search.media=0%26search.searchdate=all%26search.exact=%26search.include=%26userDisplay=50%26search.exclude=%26search.option=0%26search.sortBy=date%26search.searchBy=0%26search.includeAll=%26search.query=%C7%D5%B0%DD%26search.viewtype=title%26search.page={i}"
    driver.get(chrome_url)

    driver.switch_to.frame("cafe_main")

    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')

    results = bs.find_all('a', {'class':'article'})

    for title in results:
        word_list.append(title.text.replace('  ','').replace('\n',''))

driver.quit()

string = ''.join(word_list)

hnn = Hannanum()
name_tag = hnn.pos(string)

list = []

for word, tag in name_tag:
        if tag in ['N']:
            if word.find('주') >= 0:
                list.append(word)
            if word.find('시간') >= 0:
                list.append(word)
            if word.find('일') >= 0:
                list.append(word)
            if word.find('점') >= 0:
                list.append(word)        

counts = Counter(list)
words = counts.most_common(20)
words_dict = dict(words)

print(words_dict)


# 한글을 분석하기 위해 font를 한글로 지정, macOS는 .otf, windows 는 .ttf 파일의 위치를 지정
if platform.system() == 'Windows':
    path = r'C:\Users\kdp\AppData\Local\Microsoft\Windows\Fonts\NanumBarunpenR.ttf'

img_mask = np.array(Image.open('book.jpg'))
wc = WordCloud(font_path=path, width=400, height=400, background_color='white',
               max_font_size=200, repeat=True, colormap='tab20b', mask=img_mask)
cloud = wc.generate_from_frequencies(words_dict)

# 생성된 Wordcloud를 test.jpg로 보낸다,
# cloud.to_file('test.jpg')
plt.figure(figsize=(10,8))
plt.axis('off')
plt.title('SQLD 합격 후기 형태소 분석', fontweight = 'bold')
plt.imshow(cloud)
plt.show()


# ADsP 게시글 제목 받기 -----------------------------------------------------------------------------
word_list = []
for i in range(1,20):
    chrome_url=f"https://cafe.naver.com/sqlpd?iframe_url=/ArticleSearchList.nhn%3Fsearch.clubid=21771779%26search.menuid=132%26search.media=0%26search.searchdate=all%26search.defaultValue=1%26userDisplay=50%26search.option=0%26search.sortBy=date%26search.searchBy=0%26search.query=%C7%D5%B0%DD%26search.viewtype=title%26search.page={i}"
    driver.get(chrome_url)

    driver.switch_to.frame("cafe_main")

    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')

    results = bs.find_all('a', {'class':'article'})

    for title in results:
        word_list.append(title.text.replace('  ','').replace('\n',''))

driver.quit()

string = ''.join(word_list)

hnn = Hannanum()
name_tag = hnn.pos(string)

list = []

for word, tag in name_tag:
        if tag in ['N']:
            if word.find('주') >= 0:
                list.append(word)
            if word.find('시간') >= 0:
                list.append(word)
            if word.find('일') >= 0:
                list.append(word)
            if word.find('점') >= 0:
                list.append(word)        

counts = Counter(list)
words = counts.most_common(20)
words_dict = dict(words)

print(words_dict)


# 한글을 분석하기 위해 font를 한글로 지정, macOS는 .otf, windows 는 .ttf 파일의 위치를 지정
if platform.system() == 'Windows':
    path = r'C:\Users\kdp\AppData\Local\Microsoft\Windows\Fonts\NanumBarunpenR.ttf'

img_mask = np.array(Image.open('book.jpg'))
wc = WordCloud(font_path=path, width=400, height=400, background_color='white',
               max_font_size=200, repeat=True, colormap='twilight_shifted', mask=img_mask)
cloud = wc.generate_from_frequencies(words_dict)

# 생성된 Wordcloud를 test.jpg로 보낸다,
# cloud.to_file('test.jpg')
plt.figure(figsize=(10,8))
plt.axis('off')
plt.title('ADsP 합격 후기 형태소 분석', fontweight = 'bold')
plt.imshow(cloud)
plt.show()


# # 빅분기 게시글 제목 받기 -----------------------------------------------------------------------------
# word_list = []
# for i in range(1,12):
#     chrome_url=f"https://cafe.naver.com/sqlpd?iframe_url=/ArticleSearchList.nhn%3Fsearch.clubid=21771779%26search.menuid=136%26search.media=0%26search.searchdate=all%26search.exact=%26search.include=%26userDisplay=50%26search.exclude=%26search.option=0%26search.sortBy=date%26search.searchBy=0%26search.includeAll=%26search.query=%C7%D5%B0%DD%26search.viewtype=title%26search.page={i}"
#     driver.get(chrome_url)

#     driver.switch_to.frame("cafe_main")

#     html = driver.page_source
#     bs = BeautifulSoup(html, 'html.parser')

#     results = bs.find_all('a', {'class':'article'})

#     for title in results:
#         word_list.append(title.text.replace('  ','').replace('\n',''))

# driver.quit()

# string = ''.join(word_list)

# hnn = Hannanum()
# name_tag = hnn.pos(string)

# list = []

# for word, tag in name_tag:
#         if tag in ['N']:
#             if word.find('주') >= 0:
#                 list.append(word)
#             if word.find('시간') >= 0:
#                 list.append(word)
#             if word.find('일') >= 0:
#                 list.append(word)
#             if word.find('점') >= 0:
#                 list.append(word)        

# counts = Counter(list)
# words = counts.most_common(20)
# words_dict = dict(words)

# print(words_dict)


# # 한글을 분석하기 위해 font를 한글로 지정, macOS는 .otf, windows 는 .ttf 파일의 위치를 지정
# if platform.system() == 'Windows':
#     path = r'C:\Users\kdp\AppData\Local\Microsoft\Windows\Fonts\NanumBarunpenR.ttf'

# img_mask = np.array(Image.open('book.jpg'))
# wc = WordCloud(font_path=path, width=400, height=400, background_color='white',
#                max_font_size=200, repeat=True, colormap='Dark2', mask=img_mask)
# cloud = wc.generate_from_frequencies(words_dict)

# # 생성된 Wordcloud를 test.jpg로 보낸다,
# # cloud.to_file('test.jpg')
# plt.figure(figsize=(10,8))
# plt.axis('off')
# plt.title('빅분기 합격 후기 형태소 분석', fontweight = 'bold')
# plt.imshow(cloud)
# plt.show()