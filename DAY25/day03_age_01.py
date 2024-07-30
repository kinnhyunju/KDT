import csv
f=open('age.csv', encoding= 'euc_kr')
data = csv.reader(f)
header = next(data)

print('---------------------------------------------')
print(' age.csv index')
print('---------------------------------------------')

for i in range(len(header)):
    print(f'[{i:3}]: {header[i]}') # {1:3}: 3자리의 공간에 i값 출력


# --------------------------------------------------------------------------------
# 대구 산격동 인구 현황
for row in data:
    if '산격3동' in row[0]:     # '산격3동'이 포함된 자료만 출력
        print(row)
    
f.close()

# --------------------------------------------------------------------------------
# 대구시 산격3동의 인구 분포 그래프 그리기
import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib

f=open('age.csv', encoding= 'euc_kr')
data = csv.reader(f)
result = []
city = ''

for row in data:
    if '산격3' in row[0]:
        str_list = re.split('[()]', row[0])
        city = str_list[0]
        for data in row[3:]:
            data = data.replace(',','')
            result.append(int(data))

f.close()
print(result)

plt.title(f'{city} 인구 현황')
plt.xlabel('나이')
plt.ylabel('인구수')
plt.plot(result)
plt.show()
