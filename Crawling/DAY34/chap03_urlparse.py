from urllib.parse import urlparse

# 검색어 한글로 쓰고 싶을때 quote 설치
from urllib.parse import quote


urlString1 = 'https://shopping.naver.com/home/p/index.naver'

url = urlparse(urlString1)
print(url.scheme)
print(url.netloc)
print(url.path)

# 네이버 블로그 검색
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

query = 'ChatGPT'
url = f'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=ChatGPT'

html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

blog_results = soup.select('a.title_link')
print('검색 결과수: ',len(blog_results))    # 검색 결과 타이틀

search_count = len(blog_results)
desc_results = soup.select('a.dsc_link')    # 검색 결과의 간단한 설명

# for blog_ttile in blog_results:
#     title = blog_ttile.text
#     link = blog_ttile['href']
#     print(f'{title}, [{link}]')

for i in range(search_count):
    title = blog_results[i].text
    link = blog_results[i]['href']
    print(f'{title}, [{link}]')
    print(desc_results[i].text)
    print('-'*80)