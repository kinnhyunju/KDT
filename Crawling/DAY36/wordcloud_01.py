from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import platform
import numpy as np
from PIL import Image

text = open('test.txt', encoding='utf-8').read()
okt = Okt()

# okt 함수를 통해 읽어들인 내용의 형태소를 분석
sentence_tag = []
sentence_tag = okt.pos(text)

noun_adj_list = []
# tag가 명사이거나 형용사인 단어들만 noun_adj_list에 넣어준다
for word, tag in sentence_tag:
    if tag in ['Noun', 'Adjective']:
        noun_adj_list.append(word)
print(noun_adj_list)

# 가장 많이 나온 단어부터 50개 저장
counts = Counter(noun_adj_list)
tags = counts.most_common(50)
print(tags)

# 한글을 분석하기 위해 font를 한글로 지정, macOS는 .otf, windows 는 .ttf 파일의 위치를 지정
if platform.system() == 'Windows':
    path = r'c:\Windows\Fonts\malgun.ttf'

img_mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path=path, width=400, height=400, background_color='white',
               max_font_size=200, repeat=True, colormap='inferno', mask=img_mask)
cloud = wc.generate_from_frequencies(dict(tags))

# 생성된 Wordcloud를 test.jpg로 보낸다,
# cloud.to_file('test.jpg')
plt.figure(figsize=(10,8))
plt.axis('off')
plt.imshow(cloud)
plt.show()