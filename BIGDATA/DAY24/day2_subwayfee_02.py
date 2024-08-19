# -----------------------------------------------------------------------
# 유임 승차 비율이 50% 이하인 역
# -----------------------------------------------------------------------
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f=open('subwayfee.csv',encoding='utf-8-sig')
data = csv.reader(f)
header = next(data) # 한 줄을 읽고 다음 줄로 이동
print(header)

min_rate = 100
min_row = []
min_total_count = 0 

for row in data:
    for i in [4,6]:
        row[i] = int(row[i])
    total_count = row[4]+row[6]

    if (row[6]!=0) and (total_count>10000):
        rate = row[4] / total_count
        if rate <=0.5:
            print(row, round(rate,2))
            if rate<min_rate:
                min_rate = rate
                min_row = row
                min_total_count = total_count
f.close()

print()
print(f'유임 승차 비율이 가장 낮은 역 : {min_row[3]}')
print(f'전체 인원 : {min_total_count}명, '
      f'유임 승차 인원 : {min_row[4]:,}명, '
      f'유임 승차 비율 : {round(min_rate*100,1)}%')

plt.title(min_row[3]+"역 유,무임 승차 비율")
label = ['유임 승차', '무임 승차']
values = [min_row[4],min_row[6]]
plt.pie(values,labels=label,autopct='%1.f%%')
plt.legend(loc=2)
plt.show()

# -----------------------------------------------------------------------
# 승,하차 인원이 가장 많은 역은?
# -----------------------------------------------------------------------
max = [0]*4
max_station = ['']*4
label = ['유임승차', '유임하차', '무임승차','무임하차']

with open('subwayfee.csv',encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)

    for row in data:
        for i in range(4,8):
            row[i] = int(row[i])
            if row[i]>max[i-4]:
                max[i-4] = row[i]
                max_station[i-4] = row[3]+' '+row[1]

for i in range(4):
    print(f'{label[i]}: {max_station[i]} {max[i]:,}명')

# -----------------------------------------------------------------------
# 전체 지하철역 승,하차 인원 분석 및 파이차트 저장
# -----------------------------------------------------------------------

label = ['유임승차', '유임하차', '무임승차','무임하차']
color_list  = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
pic_count = 0
with open('subwayfee.csv',encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)

    for row in data:
        for i in range(4,8):
            row[i] = int(row[i]) 
        print(row)
        
        plt.figure(dpi=100)
        plt.title(row[3]+' '+row[1])
        plt.pie(row[4:8], labels=label, colors=color_list, autopct='%.1f%%', shadow=True)
        plt.savefig('img/'+row[3]+' '+row[1]+'.png')
        plt.close()

        pic_count +=1
        if pic_count>=10:
            break
