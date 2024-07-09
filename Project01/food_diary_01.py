def diary_menu():
    print('*'*30)
    print(f"{'식  단  일  기':^26}")
    print('*'*30)
    print(f"    1. {'기초 대사량 계산':^12}")
    print(f"    2. {'오늘 먹은 음식 추가':^12}")
    print(f"    3. {'오늘 먹은 음식 삭제':^12}")
    print(f"    4. {'오늘 먹은 음식 보기':^12}")
    print(f"    5. {'식단 일기 종료':^12}")
    print('*'*30)

def man_rate(height,weight,age):
    rate = 66.47 + (13.75 * weight) + (5* height) - (6.76 * age)
    return rate
def woman_rate(height,weight,age):
    rate = 655.1 + (9.56 * weight) + (1.85 *height) - (4.68 * age)
    return rate

# 식단 목록, 섭취 칼로리 기록
food_list = {}
food_kcal = 0
# 프로그램 실행
while True:
    diary_menu()
    choice = input("실행할 메뉴의 번호를 선택해주세요.:")
    if choice.isdecimal():
        choice = int(choice)
    else:
        print('1~5 사이 숫자만 입력하세요.')
        continue
    
    # 종료 조건 처리
    if choice == 5:
        print('식단 일기를 종료합니다.')
        break

    elif choice == 1:
        # 기초대사량 기록
        rate = 0
        print(f"{'기초대사량 계산':-^24}")
        gender = input("당신의 성별을 선택하세요\n    1. 남     2. 여\n선택 : ")
        if gender == '1':
            height = int(input("신장(cm) : "))
            weight = int(input("체중(kg) : "))
            age = int(input("나이(만) : "))
            rate = rate + 66.47 + (13.75 * weight) + (5* height) - (6.76 * age)
            print(f"당신의 기초대사량은 {round(rate)}kcal입니다.")
        elif gender == '2':
            height = int(input("신장(cm) : "))
            weight = int(input("체중(kg) : "))
            age = int(input("나이(만) : "))
            rate = rate + 655.1 + (9.56 * weight) + (1.85 *height) - (4.68 * age)
            print(f"당신의 기초대사량은 {round(rate)}kcal입니다.")
        else: 
            print(f"{gender}번은 해당되지 않습니다.성별을 다시 선택해 주세요.")

    

    elif choice == 2:
        print(f"{'오늘 먹은 음식 추가':-^24}")
        key = input("오늘 먹은 음식을 입력하세요 : ")
        value = input("음식의 칼로리를 입력하세요 : ")
        food_list.setdefault(key,value)

    elif choice == 3:
        print(f"{'오늘 먹은 음식 삭제':-^24}")
        print(f'{"오늘 먹은 음식":-^20}')
        for food in food_list:
            print(f'{food:^24}')
        d_food = input("삭제할 음식을 골라주세요 : ")
        del food_list[d_food]

    
    elif choice == 4:
        print(f"{'오늘 먹은 음식 보기':-^24}")
        if not len(food_list) : print(f'{"아직 기록된 음식이 없습니다.":^20}')
        else :
            print(f'{"오늘 먹은 음식":-^20}')
            for food in food_list:
                print(f'{food:^24}')
            calories = list(map(int,food_list.values()))
            for i in calories:
                food_kcal = food_kcal + i
            print(f"총 섭취 칼로리는 {food_kcal}kcal입니다.")
            print(f'기초대사량 대비 {(food_kcal/rate)*100:.2f}% 섭취하였습니다.')
    

    else: print(f'선택하신 {choice}번에 해당하는 메뉴가 존재하지 않습니다.')