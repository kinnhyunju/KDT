html_example = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link" href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_example, 'html.parser')
print(soup.find('div'))
print()

print(soup.find('div',{'id':'text_id2'}))

div_text = soup.find('div',{'id':'text_id2'})
print(div_text.text)
print(div_text.string)
print(div_text.get_text())
print()

href_link = soup.find('a',{'class':'internal_link'})    # 딕셔너리 형태
href_link = soup.find('a',class_='internal_link')       # class_사용 : class 는 파이썬의 예약어

print(href_link)
print(href_link['href'])            # <a> 태그 내부 href 속성의 값(url)을 추출
print(href_link.get('href'))
print(href_link.text)               # <a> Page1 </a>태그 내부의 텍스트(Page1) 추출
print()

print('href_link.attrs', href_link.attrs)
print('class 속성값:', href_link['class'])
print('values():', href_link.attrs.values())

values = list(href_link.attrs.values())
print(f'values[0]: {values[0]}, values[1]:{values[1]}')
print()

href_value = soup.find(attrs={'href':'www.google.com'})
href_value = soup.find('a',attrs={'href':'www.google.com'})
print('hrfefvalue:', href_value)
print(href_value['href'])
print(href_value.string)
print()

span_tag = soup.find('span')
print('span_tag:',span_tag)
print('attrs:',span_tag.attrs)
print('value:',span_tag.attrs['class'])
print('text:',span_tag.text)
print()

div_tags = soup.find_all('div')
print('div_tags length:',len(div_tags))
for div in div_tags : 
    print('-'*40)
    print(div)
print()

links = soup.find_all('a')
for alink in links:
    print(alink)
    print(f"url: {alink['href']}, text: {alink.string}")
    print()

link_tags = soup.find_all('a',{'class':['external_link', 'internal_link']})
print(link_tags)
print()
p_tags = soup.find_all('p', {'id':['first', 'third']})
for p in p_tags: print(p)
print()
