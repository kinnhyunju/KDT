# 미세먼지 데이터 확인
import pandas as pd
from tabulate import tabulate 

# dust 엑셀파일 불러오기
dust = pd.read_excel('dust.xlsx')

# 데이터 읽어오기
print(dust.head())
print(tabulate(dust.head(), headers='keys', tablefmt='pretty'))

# 미세먼지 데이터 구조 확인
print(dust.info())

# ------------------------------------------------------------------------------
# 미세먼지 데이터 가공
# ------------------------------------------------------------------------------
# 컬럼 이름 변경
dust.rename(columns={'날짜':'date','아황산가스':'so2', '일산화탄소':'co', '오존':'o3', '이산화질소':'no2'}, inplace=True)
print(tabulate(dust.head(), headers='keys',tablefmt='psql'))

# 날짜 데이터 변경
dust['date'] = dust['date'].str[:10]
print(tabulate(dust.head(), headers='keys', tablefmt='psql'))

# ['date'] 자료형 변경
dust['date'] = pd.to_datetime(dust['date'])
print(dust.dtypes)

# 컬럼 순서 변경
dust['year'] = dust['date'].dt.year
dust['month'] = dust['date'].dt.month
dust['day'] = dust['date'].dt.day
print(dust.columns)

dust = dust[['date', 'year', 'month','day', 'so2', 'co', 'o3', 'no2', 'PM10', 'PM2.5']]
print(dust.columns)

# ------------------------------------------------------------------------------
# 미세먼지 데이터 전처리
# ------------------------------------------------------------------------------
# 누락값(결측치) 확인
print(' 결측치 개수 확인하기')
print(dust.isna().sum())

print(' 결측치를 포함한 데이터 출력')
print(dust[dust.isna().any(axis=1)])
# any() : boolean값을 모두 return해주는 내장함수, 이 경우에 axis=0이면 오류 발생

# 결측치 채우기
print('결측치 채우기')
dust.ffill(inplace=True)    # 이전 값으로 결측치 채움
print(dust.isnull().sum())
print(dust.iloc[132:134])   # 이전 결측치의 index를 다시 출력해서 확인

# ------------------------------------------------------------------------------
# 날씨 데이터 읽기 및 확인
# ------------------------------------------------------------------------------
weather = pd.read_excel('weather.xlsx')
print(tabulate(weather.head(), headers='keys', tablefmt='psql'))
print(weather.info())

# ------------------------------------------------------------------------------
# 날씨 데이터 가공
# ------------------------------------------------------------------------------
# 컬럼 삭제 및 컬럼 이름 변경
weather.drop(['지점', '지점명'], axis=1, inplace=True)
weather.columns = ['date','temp','wind','rain', 'humidity']
print(tabulate(weather.head(), headers='keys', tablefmt='pretty'))

# 시간 정보 삭제
weather['date'] = pd.to_datetime(weather['date'].dt.date)
print(weather.info())
print(weather.head())

# ------------------------------------------------------------------------------
# 날씨 데이터 전처리
# ------------------------------------------------------------------------------
# 결측치 확인
print(' 날씨 데이터 결측치 개수 확인하기')
print(weather.isna().sum())

print(' 날씨 데이터에서 결측치를 포함하는 행 출력')
print(weather[weather.isna().any(axis=1)])

# 결측치 채우기
weather.ffill(inplace=True)         # 이전 값으로 결측치 채움
print(weather.isna().sum())
print(weather.iloc[[369,565,742]])  # 이전 결측치의 index의 값 비교

# 강수량 데이터 변경
print('강수량이 0인 항목을 0.01로 변경')
weather['rain'] = weather['rain'].replace(0,0.01)
print(weather['rain'].value_counts())

# ------------------------------------------------------------------------------
# 두 데이터의 크기 확인
# ------------------------------------------------------------------------------
print('dust,weather의 크기 확인')
print('dust.shape', dust.shape)
print('weather.shape',weather.shape)

# 미세먼지 데이터의 마지막 부분 확인
print(dust.iloc[740:])
# 날씨 데이터의 마지막 부분 확인
print(weather.iloc[740:])

# 미세먼지 데이터의 마지막 행 삭제 후 크기 확인
dust.drop(index=743,inplace=True)
print(dust.shape)

# ------------------------------------------------------------------------------
# 데이터 프레임 병합하기 : merge()
# ------------------------------------------------------------------------------
print('dust, weather 데이터프레임 merge')
merged_df = pd.merge(dust,weather, on='date')
print(merged_df.head())

# ------------------------------------------------------------------------------
# 데이터 분석
# ------------------------------------------------------------------------------
# 모든 요소별 상관관계 확인
pd.set_option('display.max_columns',None)   # 전체 컬럼 출력
pd.set_option('display.max_rows',None)      # 전체 행 출력
print(merged_df.corr())

# 미세먼지(PM10)와 상관 관계
print('미세먼지(PM10)와 상관 관계 분석')
corr = merged_df.corr()
print(corr['PM10'].sort_values(ascending=False)) # 내림차순 정렬

# ------------------------------------------------------------------------------
# 데이터 시각화
# ------------------------------------------------------------------------------
# 히스토그램
import matplotlib.pyplot as plt

merged_df.hist(column=['so2', 'co', 'o3', 'no2', 'PM10','PM2.5', 'temp','wind','rain', 'humidity'], bins=50, figsize=(20,15))
plt.show()

# 막대그래프 - 날짜별 PM10 농도 막대 그래프
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

plt.figure(figsize=(15,10))
daygraph = sns.barplot(x='day', y='PM10', data=merged_df)
plt.title('날짜별 PM10 농도')
plt.show()

# 히트맵 작성 - 상관계수가 0.3 이상인 항목과의 관계 확인
plt.figure(figsize=(15,10))
sns.heatmap(data=corr, annot=True, fmt='.2f', cmap='hot')
plt.show()

print(merged_df.info())