from bs4 import BeautifulSoup

html_text = '<span class="red"> Heavens! what a virulent attack! </span>'
soup = BeautifulSoup(html_text,'html.parser')

object_tag = soup.find('span')
print('object_tag:',object_tag)
print('attrs:',object_tag.attrs)
print('value:',object_tag.attrs['class'])
print('text:',object_tag.text)

# CSS 속성을 이용한 검색 ---------------------------------------------------------------
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html,'html.parser')

# 등장인물의 이름 : 녹색
name_list = soup.find_all('span',{'class':'green'})
for name in name_list:
    print(name.string)

# 특정 단어 찾기 --------------------------------------------------------------------------
prince_list = soup.find_all(string = 'the prince')
print(prince_list)
print('the prince count:',len(prince_list))

