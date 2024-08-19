import pandas as pd

from bs4 import BeautifulSoup
import requests
from konlpy.tag import Hannanum
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import platform
import numpy as np
from PIL import Image

import collections

if not hasattr(collections,'Callable'):
    collections.Callable = collections.abc.Callable

title_df = pd.read_csv('데이터 분석가 자격증_naver_blog.csv', encoding='utf-8')


title_df['title'] = title_df['title'].str.replace('<b>',"")
title_df['title'] = title_df['title'].str.replace('</b>',"")

title_list = title_df['title'].to_list()

print(title_list)

string = ''.join(title_list)

hnn = Hannanum()
name_tag = hnn.pos(string)

word_list = []
for word, tag in name_tag:
    if tag in ['N','F']:
        word_list.append(word)

counts = Counter(word_list)
words = counts.most_common(50)
words_dict = dict(words)

print(words_dict)