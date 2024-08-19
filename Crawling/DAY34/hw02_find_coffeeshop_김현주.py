import pandas as pd
from tabulate import tabulate

hollys = pd.read_csv('hollys_branches.csv')

while True:
    loc = input('검색할 매장의 지역을 입력하세요 : ')
    if loc == 'quit':
        print('종료 합니다.')
        break

    else:     
        loc_df = hollys[hollys['주소'].map(lambda x:all(l in x for l in loc.split()))]
        loc_df = loc_df.reset_index()
        loc_df.drop('index',axis=1, inplace=True)
        loc_df.index = loc_df.index+1  
        if len(loc_df)==0: print('검색된 매장이 없습니다.\n')      
        else : 
            print(f'검색된 매장 수: {len(loc_df)}')
            print(tabulate(loc_df, headers='keys', tablefmt = 'psql'))