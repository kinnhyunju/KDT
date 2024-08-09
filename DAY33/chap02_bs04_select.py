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
            <a class="external_link" href="www.naver.com">naver</a>

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
head = soup.select_one('head')
print(head)
print('head.text:',head.text.strip())
h1 = soup.select_one('h1')
print(h1)
print()

footer = soup.select_one('h1#footer')
print(footer)
print()

class_link = soup.select_one('a.internal_link')
print(class_link)
print(class_link.string)
print(class_link['href'])
print()

link1 = soup.select_one('div#link > a.external_link')
print(link1)

print('\nfind()함수와 비교')
link_find = soup.find('div',{'id':'link'})
external_link = link_find.find('a',{'class':'external_link'})
print('external_link:', external_link)


print('\n자손 관계의 하위태그')
link2 = soup.select_one('div#class1 p#second')
print(link2)
print(link2.string)
print()

internal_link = soup.select_one('div#link a.internal_link')
print(internal_link['href'])
print(internal_link.text)

print('\nselect() 함수')
h1_all = soup.select('h1')
print('h1_all:',h1_all)
print()

url_links = soup.select('a')
for link in url_links:
    print(link['href'])
print()

div_urls = soup.select('div#class1 > a')
print(div_urls)
print(div_urls[0]['href'])
print()
div_urls2 = soup.select('div#class1 a')
print(div_urls2)

print('\n여러 항목 검색하기')
h1 = soup.select('#heading, #footer')
print(h1)
print()
url_links = soup.select('a.external_link, a.internal_link')
print(url_links)