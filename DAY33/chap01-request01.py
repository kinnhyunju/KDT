# 멜론 웹사이트 접근

# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# melon_url = 'https://www.melon.com/chart/index.htm'
# html = urlopen(melon_url)

# soup = BeautifulSoup(html.read(),'html.parser')
# print(soup)
#  HTTP Error 406: Not Acceptable : 사람이 아닌 로봇으로 인식해서 크롤링을 막음 (User Agent 정보가 없음)

# ------------------------------------------------------------------------------------------------------------
# Request 클래스 사용 
# - User Agent 정보 추가 : headers={'User-Agent' : 'Mozila/5.0'}

from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup

melon_url = 'https://www.melon.com/chart/index.htm'
# HTTP request 패킷 생성 : Request()
urlrequest = Request(melon_url, headers={'User-Agent' : 'Mozila/5.0'})

html = urlopen(urlrequest)
soup = BeautifulSoup(html.read().decode('utf-8'),'html.parser')
print(soup)
