import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 데이터 불러오기
pop_DF = pd.read_csv('gender.csv',encoding='euc_kr')

# 총 인구 데이터 중 대구에 해당하는 데이터만 추출
daegu_pop_DF = pop_DF.iloc[43:53,[0,104,207]].reset_index().drop('index',axis=1)

# 시,구 이름과 성별 인구수 담을 빈 리스트 생성
city_names = []
male_population = []
female_population = []

# 시,구 이름 / 남녀별 인구수 담기
for i in range(len(daegu_pop_DF)):
    name = daegu_pop_DF.iloc[i,0].split(' (')[0]
    city_names.append(name)

    male_num = daegu_pop_DF.iloc[i,1].replace(',','')
    male_population.append(int(male_num))

    female_num = daegu_pop_DF.iloc[i,2].replace(',','')
    female_population.append(int(female_num))

# 화면에 출력할 내용 : {동네} : (남:{남자인구} 여:{여자인구})
for i in range(len(city_names)):
    print(f'{city_names[i]}: (남:{male_population[i]:,} 여:{female_population[i]:,})')


# 파이차트 그리기
sum_population = []
for i in range(len(male_population)):
    sum_population.append((male_population[i],female_population[i]))
fig = plt.figure(figsize=(8,15))
graph = fig.subplots(5,2)

for i in range(5):
    for j in range(2) :
        graph[i,j].pie(sum_population[2*i+j],labels = ['남성','여성'], autopct='%.1f%%',startangle=90)
        graph[i,j].set_title(city_names[2*i+j])

plt.suptitle('대구광역시 구별 남녀 인구 비율')
plt.show()
