import pymysql
import pandas as pd
import csv

import pymysql.cursors

conn = pymysql.connect(host='localhost', user = 'root', password = '1234',
                       db='sakila', charset='utf8')

cur = conn.cursor()
cur.execute('select * from language')

desc = cur.description  # 헤더 정보 가져옴
for i in range(len(desc)): print(desc[i][0], end = ' ')
print()

rows = cur.fetchall()   # 모든 데이터 가져옴
for data in rows : print(data)
print()

cur.close()
conn.close()            # 데이터베이스 연결 종료

# ---------------------------------------------------------------------------------------------
conn = pymysql.connect(host='localhost', user = 'root', password = '1234',
                       db='sakila', charset='utf8')
cur1 = conn.cursor(pymysql.cursors.DictCursor)
cur1.execute('select * from language')
rows1 = cur1.fetchall()

language_df = pd.DataFrame(rows1)
print(language_df)
print()
print(language_df['name'])
cur.close()
conn.close()

# ---------------------------------------------------------------------------------------------
