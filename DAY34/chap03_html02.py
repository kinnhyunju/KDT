from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html,'html.parser')

table_tag = soup.find('table',{'id':'giftList'})
print('children 개수: ',len(list(table_tag.children)))

index = 0
for child in table_tag.children:
    index+=1
    print(f'[{index}]: {child}')
    print('-'*30)

# 트리이동 : 자손 (descendants)
desc = soup.find('table',{'id':'giftList'}).descendants
list_desc = list(desc)
print('descendants 개수:', len(list_desc))

for tag in list_desc:
    print(tag)

# 트리이동 : 형제 다루기
for sibling in soup.find('table',{'id':'giftList'}).tr.next_siblings:       # next_siblings
    print(sibling)
    print('-'*30)

print('\nprevious_siblngs')
for sibling in soup.find('tr',{'id':'gift2'}).previous_siblings:            # previous_siblings
    print(sibling)

# next_sibling, previous_sibling
sibling1 = soup.find('tr',{'id':'gift3'}).next_sibling
print('sibling1:',sibling1)
print(ord(sibling1))
print()

sibling2 = soup.find('tr',{'id':'gift3'}).next_sibling.next_sibling
print('sibling2:\n',sibling2)

# 트리이동 : 부모 다루기
style_tag = soup.style
print(style_tag.parent)

img1 = soup.find('img',{'src':'../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
print(text)