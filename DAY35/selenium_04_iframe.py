from bs4 import BeautifulSoup
from selenium import webdriver
# AttributeError: module 'collections' has no attribute 'Callable' 오류 발생시 추가 ----
import collections

if not hasattr(collections,'Callable'):
    collections.Callable = collections.abc.Callable
#--------------------------------------------------------------------------------------

driver =  webdriver.Chrome()
driver.get('https://blog.naver.com/swf1004/221631056531')

driver.switch_to.frame('mainFrame')

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

results = soup.find_all('div',{'class':'se-module'})

result1 = []
for result in results:
    remove_carriage_str = result.text.replace('\n','')
    print(remove_carriage_str)
    result1.append(remove_carriage_str)