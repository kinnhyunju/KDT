from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import Request

import matplotlib.pyplot as plt
import koreanize_matplotlib

import pandas as pd
from tabulate import tabulate

import collections
if not hasattr(collections,'Callable'):
    collections.Callable = collections.abc.Callable

company_list = []
money_list = []

for i in range(1,11):
    url = f'https://www.saramin.co.kr/zf_user/salaries/industry/it-list?page={i}&order=rank&industry_cd=it&company_cd=&rec_status=y&group_cd=0&search_company_nm_org=&search_company_nm=&min_salary=1000&max_salary=10000&request_modify_company_nm='
    urlrequest = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(urlrequest)
    bs = BeautifulSoup(html, 'html.parser')

    company = bs.find_all('a',{'class':'link_tit'})
    for name in company:
        company_list.append(name.text)

    money = bs.select('span.txt_avg')
    for num in money[5:]:
        money_list.append(int(num.text.replace(',','')))

money_dict = dict(zip(company_list, money_list))

sorted_dict = dict(sorted(money_dict.items(), key = lambda x : x[1], reverse=True))

money_key = list(sorted_dict.keys())
money_value = list(sorted_dict.values())

money_df = pd.DataFrame(zip(money_key, money_value))
money_df.columns=['기업 명', '연봉']
money_df.to_csv('income.csv',index=False)