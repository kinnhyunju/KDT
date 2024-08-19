# 대구 기온 데이터에서 시작 연도, 마지막 연도를 입력하고 특정 월의 최고 기온 및 최저 기온의 평균값을 구하고 그래프로 표현
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib


def draw_graph_max_min(title,year,max_list,min_list):
    plt.rc('axes',unicode_minus=False)
    plt.figure(figsize=(20,6))
    plt.plot(year,min_list,'b',marker = 's', label = '최저기온')
    plt.plot(year,max_list,'r',marker = 's', label = '최고기온')
    plt.xticks(year)
    plt.title(title)
    plt.legend()
    plt.show()

def temp():
    start_y = int(input('시작 연도를 입력하세요: '))
    stop_y = int(input('마지막 연도를 입력하세요: '))
    search_m = int(input('기온 변화를 측정할 달을 입력하세요: '))

    weather_df = pd.read_csv('daegu-utf8-df.csv',encoding = 'utf-8-sig')
    weather_df['날짜'] = pd.to_datetime( weather_df['날짜'], format='%Y-%m-%d')

    years = stop_y-start_y+1
    max_list = [0]*years
    min_list = [0]*years

    for i in range(years):
        target_df = weather_df[(weather_df['날짜'].dt.year==start_y+i)&
                                 (weather_df['날짜'].dt.month==search_m)]
        max_list[i] = round(target_df['최고기온'].mean(),1)
        min_list[i] = round(target_df['최저기온'].mean(),1)

    print(f'{start_y}년부터 {stop_y}년까지 {search_m}월의 기온 변화')
    print(f'{search_m}월 최저 기온 평균:\n{min_list}')
    print(f'{search_m}월 최고 기온 평균:\n{max_list}')

    year = [y for y in range(start_y,stop_y+1)]
    draw_graph_max_min(f'{start_y}년부터 {stop_y}년까지 {search_m}월의 기온 변화',year,max_list,min_list)


temp()