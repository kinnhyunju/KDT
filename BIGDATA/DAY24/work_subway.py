import csv
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

with open('subwaytime.csv',encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    station_line = []
    max_station = ['']*7
    max_passenger = [0]*7
    max_list = ['']*7


    for i in range(1,8):
        station_line.append(str(i)+'호선')

    for row in data:
        row[4:] = map(int, row[4:])
        for i in range(7) :
            if row[1] == station_line[i]:
                if max_passenger[i] < row[11]+row[13]:
                    max_passenger[i] = row[11]+row[13]
                    max_station[i] = row[3]

    for i in range(7):
        max_list[i] = station_line[i]+' '+max_station[i]
        print(f'출근 시간대 {station_line[i]} 최대 하차역 : {max_station[i]}역, 하차 인원 {max_passenger[i]:,}명')

    plt.bar(range(7),max_passenger)
    plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역')
    plt.xticks(range(7),labels=max_list, rotation = 70)
    plt.tight_layout()
    plt.show()