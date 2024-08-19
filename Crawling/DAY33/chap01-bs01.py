from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('http://www.pythonscraping.com/pages/error.html')    
except HTTPError as e : print(e)
except URLError as e : print('The server could not be found!')
else : print('It worked!')

# -----------------------------------------------------------------------------
# 존재하지 않는 태그 예외 처리

from bs4 import BeautifulSoup

def getTitle(url,tag):
    try:
        html = urlopen(url)
    except HTTPError as e : return None

    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        value = bsObj.find(tag)
    except AttributeError as e : return None
    return value

tag = 'h2'
value = getTitle('http://www.pythonscraping.com/pages/page1.html',tag)

if value == None : 
    print(f'{tag} could not be found')
else :
    print(value)