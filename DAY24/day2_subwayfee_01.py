# -----------------------------------------------------------------------
# 대중교통 데이터 읽어오기
# -----------------------------------------------------------------------
import csv

f=open('subwayfee.csv',encoding='utf-8-sig')
data = csv.reader(f)
header = next(data) # 한 줄을 읽고 다음 줄로 이동
print(header)
i = 1
for row in data:
    print(row)
    if i>5 : 
        break
    i +=1
f.close()

# -----------------------------------------------------------------------
# 전체 탑승 인원 대비 유임 승차 비율이 가장 높은 역은?
# -----------------------------------------------------------------------
# # rate = 유임 승차 인원 / 무임 승차 인원

# import csv

# f=open('subwayfee.csv',encoding='utf-8-sig')
# data = csv.reader(f)
# header = next(data) # 한 줄을 읽고 다음 줄로 이동

# max_rate = 0
# rate = 0

# for row in data:
#     for i in range(4,8):
#         row[i] = int(row[i])    # 4,5,6,7 컬럼 값을 정수로 반환
#     rate = row[4] / row[6]      # [6] 컬럼의 값이 0인 행 확인 용도

#     if rate > max_rate:
#         max_rate = rate
# print(max_rate)
# f.close()

# -----------------------------------------------------------------------
# 무임 승차 인원이 0인 역 찾기 (1)
# -----------------------------------------------------------------------
# rate = 유임승차인원 / 전체 탑승 인원 (유임승차+무임승차)
import csv

f=open('subwayfee.csv',encoding='utf-8-sig')
data = csv.reader(f)
header = next(data) # 한 줄을 읽고 다음 줄로 이동
rate = 0

for row in data : 
    for i in range(4,8):
        row[i] = int(row[i])
    rate = row[4] / (row[4]+row[6])

    if row[6]==0:       # 무임승차 인원[6]이 없는 역 출력
        print(row)
f.close()

# -----------------------------------------------------------------------
# 유동인구가 10만명 이상인 최대 유임승차 인원이 있는 역은? (2)
# -----------------------------------------------------------------------
import csv

f=open('subwayfee.csv',encoding='utf-8-sig')
data = csv.reader(f)
header = next(data) # 한 줄을 읽고 다음 줄로 이동

max_rate = 0
rate = 0

max_row = []
max_total_num = 0

for row in data:
    for i in  range(4,8):
        row[i] = int(row[i])
    total_count = row[4]+row[6]

    if (row[6]!=0) and(total_count>100000):
        rate = row[4] / total_count

        if rate > max_rate :
            max_rate = rate
            max_row = row
            max_total_num = total_count

            print(f'역 이름 : {max_row[3]}, 전체 인원 : {max_total_num:,}명,'
                  f'유임 승차 인원 : {max_row[4]:,}명, '
                  f'유임 승차 비율 : {round(max_rate*100,1):,}%')
print('-'*80)
print('최대 유임 승차역')
print(f'역 이름 : {max_row[3]}, 전체 인원 : {max_total_num:,}명, '
      f'유임 승차 인원 : {max_row[4]:,}명, '
      f'유임 승차 비율 : {round(max_rate*100,1):,}%')
f.close