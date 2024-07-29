# -----------------------------------------------------------------------
# 출근 시간대 승차 인원이 많은 10개의 역 이름 찾기
# -----------------------------------------------------------------------
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

with open('subwaytime.csv',encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)

    station_list = []
    max_num = -1
    max_station = ''

    for row in data:
        row[4:] = map(int, row[4:])
        passenger_num = sum(row[10:15:2])

        station_name = row[3]+'('+ row[1] +')'
        station_list.append((station_name,passenger_num))

sorted_passenger_list = sorted(station_list, key = lambda x : x[1], reverse=True)

index = 1
for station in sorted_passenger_list[:10]:
    print(f'[{index}] : {station[0]} {station[1]:,}')
    index+=1

station_name, station_passenger = zip(*sorted_passenger_list[:10])


plt.figure(figsize=(8,6))
plt.title('출근 시간 대 승차 인원이 가장 많은 10개 역', size = 16)

plt.bar(range(len(station_passenger)), station_passenger)
plt.xticks(range(len(station_name)),station_name, rotation = 70, fontsize = 8)
plt.ylabel('승차인원수')
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------
# 시간대별 가장 많이 승차하는 역 정보 분석
# -----------------------------------------------------------------------
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

with open('subwaytime.csv',encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    max = [0]*23
    max_station = ['']*23
    xtick_list = []

    for i in range(4,27):
        n = i%24
        xtick_list.append(str(n))

    for row in data:
        row[4:] = map(int,row[4:])
        for j in range(23):
            a = row[4+j*2]

            if a > max[j]:
                max[j] = a
                max_station[j] = xtick_list[j] + '시' + row[3]
    
    for i in range(len(max)):
        print(f'[{max_station[i]}] : {max[i]:,}명')

plt.figure(figsize=(10,10))
plt.title('시간대별 최대 승차역 정보')
plt.bar(range(23), max)
plt.xticks(range(23), labels=max_station, rotation = 80)
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------
# 모든 지하철역에서 시간대별 승하차 인원
# -----------------------------------------------------------------------
with open('subwaytime.csv',encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    subway_in = [0]*24
    subway_out = [0]*24

    for row in data:
        row[4:] = map(int,row[4:])

        for i in range(24):
            subway_in[i] += row[4+i*2]
            subway_out[i] += row[5+i*2]

xtick_list = []
for i in range(4,28):
    n = i%24
    xtick_list.append(str(n))

plt.figure(dpi=100)
plt.title('지하철 시간대별 승하차 인원 추이',size=16)
plt.grid(linestyle = ':')   # 그리드 라인 표시
plt.plot(subway_in, label = '승차')
plt.plot(subway_out, label = '하차')
plt.legend()

plt.xticks(range(24), labels=xtick_list)
plt.xlabel('시간')
plt.ylabel('인원 (천만명)')
plt.show()