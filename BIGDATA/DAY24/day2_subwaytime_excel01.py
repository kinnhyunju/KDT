# -----------------------------------------------------------------------
# 지하철 시간대별 이용현황 : 엑셀 파일 및 Pandas 활용
# -----------------------------------------------------------------------
import pandas as pd
from tabulate import tabulate

# 지하철 시간대별 이용현황
df = pd.read_excel('subway.xls', sheet_name='지하철 시간대별 이용현황', header=[0,1])
print(df.head())
# print(tabulate(df.head(), headers='keys', tablefmt='pretty'))

# 모든 컬럼 내용 확인
print(df.columns)

# 특정 컬럼 데이터 가져오기 : 호선명
print(df[('호선명',  'Unnamed: 1_level_1')])
# 특정 컬럼 데이터 가져오기 : 지하철역
print(df[('지하철역',  'Unnamed: 3_level_1')])

# DataFrame에서 여러 컬럼 선택
commute_time_df = df.iloc[:,[1,3,10,12,14]]
print(tabulate(commute_time_df.head(), headers='keys',tablefmt='pretty'))

# 모든 컬럼의 데이터 타입 확인
print(commute_time_df.dtypes)

# 천단위 콤마 제거
commute_time_df[('07:00:00~07:59:59','승차')] = commute_time_df[('07:00:00~07:59:59','승차')].apply(lambda x :x.replace(',',''))
commute_time_df[('08:00:00~08:59:59','승차')] = commute_time_df[('08:00:00~08:59:59','승차')].apply(lambda x :x.replace(',',''))
commute_time_df[('09:00:00~09:59:59','승차')] = commute_time_df[('09:00:00~09:59:59','승차')].apply(lambda x :x.replace(',',''))

print(tabulate(commute_time_df.head(), headers='keys',tablefmt='psql'))

# 데이터 타입 변경
commute_time_df = commute_time_df.astype({('07:00:00~07:59:59','승차'):'int64'})
commute_time_df = commute_time_df.astype({('08:00:00~08:59:59','승차'):'int64'})
commute_time_df = commute_time_df.astype({('09:00:00~09:59:59','승차'):'int64'})
print(commute_time_df.dtypes)

# 각 행(지하철역)의 승차 인원 수 합 계산
row_sum_df = commute_time_df.sum(axis=1,numeric_only=True)
passenger_number_list = row_sum_df.to_list()
print(row_sum_df)

# 최대값 및 최대값 인덱스 찾기
max_number = row_sum_df.max(axis=0)     # 해당 열에서 최대값 찾기
print(max_number)

max_index = row_sum_df.idxmax()
max_line, max_station = df.iloc[max_index,[1,3]]

print(f'출근 시간대 최대 승차 인원역 : {max_line} {max_station} {max_number}명')