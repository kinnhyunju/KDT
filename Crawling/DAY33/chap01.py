from urllib.request import urlopen

html = urlopen('https://www.daangn.com/hot_articles')
print(type(html))
print(html.read())

# -----------------------------------------------------------------------------
# Beautiful Soup 라이브러리
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs)
print(bs.h1)          # <h1> 텍스트 </h1> : 태그까지 다 가지고 옴
# print(bs.h1.string) # .text => .string : 태그 내부의 문자열만 가져옴

'''
<html>
<head>
<title>A Useful Page</title>
</head>
<body>
<h1>An Interesting Title</h1>
<div>
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</div>
</body>
</html>
'''
# head : 속성, 타이틀 기입 (페이지에 나타나지는 않음)
# body : 본문 내용
# h1 : 시작
# <태그> & </태그> : '/' 넣어서 항상 짝꿍으로 마무리

