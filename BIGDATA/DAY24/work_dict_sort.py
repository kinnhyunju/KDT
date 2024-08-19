def menu():
    print('-'*40)
    print('1. 전체 데이터 출력')
    print('2. 수도 이름 오름차순 출력')
    print('3. 모든 도시의 인구수 내림차순 출력')
    print('4. 특정 도시의 정보 출력')
    print('5. 대륙별 인구수 계산 및 출력')
    print('6. 프로그램 종료')
    print('-'*40)

Dic_country = {'Seoul':['South Korea','Asia',9655000], 'Tokyo':['Japan','Asia',14110000],
               'Beijing':['China','Asia',21540000], 'London':['United Kingdom','Europe',14800000],
               'Berlin':['Germany','Europe',3426000], 'Mexico City':['Mexico','America',21200000]}

cities = list(Dic_country.keys())
values = list(Dic_country.values())

while True:
    menu()
    choice = int(input('메뉴를 입력하세요: '))

    if choice == 6:
        print('프로그램을 종료합니다.')
        break

    elif choice == 1:
        for i in range(len(Dic_country)):
            print(f'[{i+1}] {cities[i]}: {values[i]}')

    elif choice == 2:
        sort_dict = sorted(Dic_country.items())
        for idx,(key,value) in enumerate(sort_dict):
            print(f'[{idx+1}] {key:11} : {value[0]:16} {value[1]:9} {value[2]:>10,}')

    elif choice == 3 :
        sort_dict2 = sorted(Dic_country.items(), key=lambda x : x[1][2], reverse= True)
        for idx,(key,value) in enumerate(sort_dict2):
            print(f'[{idx+1}] {key:11} : {value[2]:>13,}')

    elif choice == 4:
        city = input('출력할 도시 이름을 입력하세요 : ')
        if city not in cities : print(f'도시이름 : {city}은 key에 없습니다.')
        else : print(f'도시:{city}\n국가:{values[cities.index(city)][0]}, '
                     f'대륙:{values[cities.index(city)][1]}, 인구수:{values[cities.index(city)][2]:,}')

    elif choice == 5:
        continent = input('대륙 이름을 입력하세요(Asia, Europe, America): ')
        idx_list = []
        for i in range(len(values)):
            if continent in values[i][1]:
                idx_list.append(i)

        sum_pop = 0
        for i in idx_list:
            print(f'{cities[i]}: {values[i][2]:,}')
            sum_pop += values[i][2]
        print(f'{continent} 전체 인구수: {sum_pop:,}')