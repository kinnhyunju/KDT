import matplotlib.pyplot as plt
import koreanize_matplotlib

import pandas as pd
from tabulate import tabulate

# 자격증 정보 그래프
cert_df = pd.read_csv('certification.csv')
print(tabulate(cert_df, headers='keys', tablefmt='psql'))

cert_name = cert_df['자격증 이름'].to_list()
cert_num = cert_df['횟수'].to_list()

colors = ['mediumpurple', 'royalblue','mediumslateblue','cornflowerblue','orchid','lightskyblue','plum','blueviolet','slateblue','midnightblue','darkorchid','mediumblue']

plt.figure(figsize=(10,12))
data = plt.bar(cert_name, cert_num, color = colors, edgecolor = '#3c3c3c', linewidth = 1.2)
plt.bar_label(data, labels=cert_num)
plt.title('[ 데이터 분석 자격증 언급 횟수 - 2024년 ]', fontsize = 15, fontweight = 'bold')
plt.xlabel('< 자격증 이름 >', fontweight = 'bold')
plt.ylabel('< 횟수 >', fontweight = 'bold')
plt.xticks(rotation = 60)
plt.show()

# 연봉 정보 그래프
income_df = pd.read_csv('income.csv')
print(tabulate(income_df, headers='keys', tablefmt='psql'))

comp_money = income_df['연봉'].to_list()[10:-10]

top_10_name = income_df['기업 명'].to_list()[:11]
top_10_value = income_df['연봉'].to_list()[:11]

avg_num = round(sum(comp_money)/len(comp_money))
avg_num2 = round(sum(income_df['연봉'].to_list())/len(income_df['연봉'].to_list()))
print(avg_num, avg_num2)
colors = ['mediumpurple', 'royalblue','mediumslateblue','cornflowerblue','orchid','lightskyblue','plum','blueviolet','slateblue','midnightblue','darkorchid','mediumblue']

plt.figure(figsize=(10,16))
bar = plt.bar(top_10_name, top_10_value, color = colors,edgecolor = '#3c3c3c', linewidth = 1.2)
plt.bar_label(bar, labels=top_10_value)
plt.title('[ ITㆍ웹ㆍ통신업 기업 연봉 정보 ]', fontsize = 15, fontweight = 'bold')
plt.xlabel('<기업 명>', fontweight = 'bold')
plt.ylabel('<연봉 (만원)>', fontweight = 'bold')
plt.axhline(avg_num, color='k', linestyle='--', linewidth = 4)
plt.xticks(rotation = 50)
plt.show()