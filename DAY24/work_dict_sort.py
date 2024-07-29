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
               'Beijing':['China','Asia',21540000], 'London':['United	Kingdom','Europe',148000000],
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

    elif choice == 4:
        city = input('출력할 도시 이름을 입력하세요 : ')
        if city not in cities : print(f'도시이름 : {city}은 key에 없습니다.')
        else : print(f'도시:{city}\n국가:{values[cities.index(city)][0]}, '
                     f'대륙:{values[cities.index(city)][1]}, 인구수:{values[cities.index(city)][2]:,}')
