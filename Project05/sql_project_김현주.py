import pandas as pd
import pymysql
import pymysql.cursors
from tabulate import tabulate
import matplotlib.pyplot as plt
import koreanize_matplotlib

conn = pymysql.connect(host='172.20.60.116',user='member1',password='1234',
                       db = 'sql_project',charset='utf8')
cur = conn.cursor(pymysql.cursors.DictCursor)

# --------------------------------------------------------------------------------------
# 테이블 불러오기 함수
def call_table(table): 
    cur.execute(f'select * from {table}')
    rows = cur.fetchall()
    DF = pd.DataFrame(rows)
    return DF

music5000_df = call_table('popular_music_to5000')
music10000_df = call_table('popular_music_to10000')
music_ov10000_df = call_table('popular_music_over10000')

# --------------------------------------------------------------------------------------
# music10000_df, music_ov10000_df 데이터 타입 : 실수 => 정수로 변환
# 컬럼명 리스트로 받기
cols = music10000_df.columns.to_list()[1:]
# 타입 변경
music10000_df[cols] = music10000_df[cols].astype('int64')
music_ov10000_df[cols] = music_ov10000_df[cols].astype('int64')

# --------------------------------------------------------------------------------------
# 컬럼의 값을 리스트로 가져오는 함수
def value_list(DF,Column):
    value_list = DF[f'{Column}'].to_list()
    return value_list

# 지역 리스트
regions = value_list(music5000_df,'지역')
# 티켓 판매수 리스트
count_5000 = value_list(music5000_df,'총 티켓판매수')
count_10000 = value_list(music10000_df,'총 티켓판매수')
count_ov10000 = value_list(music_ov10000_df,'총 티켓판매수')

# 티켓 판매액 리스트
cost_5000 = value_list(music5000_df,'총 티켓판매액')
cost_10000 = value_list(music10000_df,'총 티켓판매액')
cost_ov10000 = value_list(music_ov10000_df,'총 티켓판매액')

# 공연 건수 리스트
open_5000 = value_list(music5000_df,'공연건수')
open_10000 = value_list(music10000_df,'공연건수')
open_ov10000 = value_list(music_ov10000_df,'공연건수')

# --------------------------------------------------------------------------------------
# # 티켓 판매 수 그래프
# x = pd.Series(range(len(music5000_df)))
# b_width = 0.3
# plt.figure(figsize=(20,10))
# to5000 = plt.bar(x-0.3, count_5000, b_width, label = '5,000명 이하 규모 공연')
# to10000 = plt.bar(x, count_10000, b_width, label = '10,000명 이하 규모 공연')
# over10000 = plt.bar(x+0.3, count_ov10000, b_width, label = '10,000명 초과 규모 공연')
# plt.xticks(x,regions)
# plt.xlabel('지역',fontsize=12)
# plt.ylabel('티켓 판매 수',fontsize=12)
# plt.bar_label(to5000, labels=count_5000)
# plt.bar_label(to10000, labels=count_10000)
# plt.bar_label(over10000, labels=count_ov10000)
# plt.legend()
# plt.title('[ 2023년 지역별 대중음악 공연 티켓 판매 수 ]', fontsize=20)
# plt.show()

# # 티켓 판매액 그래프
# x = pd.Series(range(len(music5000_df)))
# b_width = 0.3
# plt.figure(figsize=(20,10))
# to5000 = plt.bar(x-0.3, cost_5000, b_width, label = '5,000명 이하 규모 공연')
# to10000 = plt.bar(x, cost_10000, b_width, label = '10,000명 이하 규모 공연')
# over10000 = plt.bar(x+0.3, cost_ov10000, b_width, label = '10,000명 초과 규모 공연')
# plt.xticks(x,regions)
# plt.xlabel('지역',fontsize=12)
# plt.ylabel('티켓 판매액',fontsize=12)
# plt.bar_label(to5000, labels=cost_5000)
# plt.bar_label(to10000, labels=cost_10000)
# plt.bar_label(over10000, labels=cost_ov10000)
# plt.legend()
# plt.title('[ 2023년 지역별 대중음악 공연 티켓 판매 금액 ]', fontsize=20)
# plt.show()

# 공연 건수 그래프
x = pd.Series(range(len(music5000_df)))
b_width = 0.3
plt.figure(figsize=(20,10))
to5000 = plt.bar(x-0.3, open_5000, b_width, label = '5,000명 이하 규모 공연')
to10000 = plt.bar(x, open_10000, b_width, label = '10,000명 이하 규모 공연')
over10000 = plt.bar(x+0.3, open_ov10000, b_width, label = '10,000명 초과 규모 공연')
plt.xticks(x,regions)
plt.xlabel('지역',fontsize=12)
plt.ylabel('티켓 판매액',fontsize=12)
plt.bar_label(to5000, labels=open_5000)
plt.bar_label(to10000, labels=open_10000)
plt.bar_label(over10000, labels=open_ov10000)
plt.legend()
plt.title('[ 2023년 지역별 대중음악 공연 건수 ]', fontsize=20)
plt.show()

# --------------------------------------------------------------------------------------
# 공연 규모별 티켓 판매 가격 평균 구하기
region = music5000_df['지역']
small_avg = round(music5000_df['총 티켓판매액']*1000/ music5000_df['총 티켓판매수'],2)
medium_avg = round(music10000_df['총 티켓판매액']*1000/ music10000_df['총 티켓판매수'],2)
large_avg = round(music_ov10000_df['총 티켓판매액']*1000/ music_ov10000_df['총 티켓판매수'],2)

# 시리즈 합쳐서 DF로 바꾸기
avg_df = pd.concat([region,small_avg,medium_avg,large_avg],axis=1)
avg_df.fillna(0,inplace=True)

# DF => SQL 테이블로 데이터 추가
sql = '''insert into popular_avg(region,small,medium,large)
        values(%s, %s, %s, %s)'''

# for i in avg_df.index:
#     value = avg_df.loc[i].tolist()
#     cur.execute(sql,value)
#     conn.commit()

# --------------------------------------------------------------------------------------
# 티켓 판매액 그래프 그리기

# 평균 티켓 판매액 리스트 만들기
avg_5000 = avg_df[0].tolist()
avg_10000 = avg_df[1].tolist()
avg_ov10000 = avg_df[2].tolist()


x = pd.Series(range(len(avg_df)))
b_width = 0.3
plt.figure(figsize=(20,10))
to5000 = plt.bar(x-0.3, avg_5000, b_width, label = '5,000명 이하 규모 공연')
to10000 = plt.bar(x, avg_10000, b_width, label = '10,000명 이하 규모 공연')
over10000 = plt.bar(x+0.3, avg_ov10000, b_width, label = '10,000명 초과 규모 공연')
plt.xticks(x,regions)
plt.xlabel('지역',fontsize=12)
plt.ylabel('평균 티켓 판매액',fontsize=12)
plt.bar_label(to5000, labels=avg_5000)
plt.bar_label(to10000, labels=avg_10000)
plt.bar_label(over10000, labels=avg_ov10000)
plt.legend(loc='lower right', bbox_to_anchor=(1.0,1.0))
plt.title('[ 2023년 지역별 대중음악 공연 티켓 평균 판매 금액 ]', fontsize=20)
plt.show()