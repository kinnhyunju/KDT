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

# 식단 목록, 기초대사량 초기값 기록
food_list = []
rate = 0
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
        while True:
            print(f"{'기초대사량 계산':-^24}")
            gender = input("당신의 성별을 선택하세요\n    1. 남     2. 여\n선택 : ")
            
            if gender.isdecimal():
                gender = int(gender)
            else:
                print('숫자를 입력해주세요.')
                continue
            if gender == 1:
                while True:
                    info = input("신장(cm), 체중(kg), 나이(만)를 입력하세요 (예 : 130 80 50)\n입력 : ").split()
                    if len(info) ==3:
                        for i in range(len(info)):
                            if info[i].isdecimal():
                                height = int(info[0])
                                weight = int(info[1])
                                age = int(info[2])
                        rate = rate + 66.47 + (13.75 * weight) + (5* height) - (6.76 * age)
                        print(f"당신의 기초대사량은 {round(rate)}kcal입니다.")
                        break
                    else: 
                        print('예시에 맞게 신장(cm), 체중(kg), 나이(만)를 다시 입력하세요.\n')
                    continue
                break
                    

            elif gender == 2:
                while True:
                    info = input("신장(cm), 체중(kg), 나이(만)를 입력하세요 (예 : 130 80 50)\n입력 : ").split()
                    if len(info) ==3:
                        for i in range(len(info)):
                            if info[i].isdecimal():
                                height = int(info[0])
                                weight = int(info[1])
                                age = int(info[2])
                        rate = rate + 655.1 + (9.56 * weight) + (1.85 *height) - (4.68 * age)
                        print(f"당신의 기초대사량은 {round(rate)}kcal입니다.")
                        break
                    else: 
                        print('예시에 맞게 신장(cm), 체중(kg), 나이(만)를 다시 입력하세요.\n')
                    continue
                break
            else: 
                print(f"{gender}번은 해당되지 않습니다.성별을 다시 선택해 주세요.")
                continue

    

    elif choice == 2:
        print(f"{'오늘 먹은 음식 추가':-^24}")
        key = input("오늘 먹은 음식을 입력하세요 : ")
        while True:
            value = input(f"{key}의 칼로리를 입력하세요 : ")
            if value.isdecimal():
                food_list.append([key,value])
                break
            else :
                print("칼로리는 숫자로 입력해야 합니다.\n")
                continue


    elif choice == 3:
        print(f"{'오늘 먹은 음식 삭제':-^24}")
        print(f'{"오늘 먹은 음식":-^24}')
        while True:
            for i in range(len(food_list)):
                print(f'{i+1:>5}. {food_list[i][0]}    {food_list[i][1]}kcal')
            d_food = input("삭제할 음식의 번호를 입력하세요. 전체 삭제를 원하면 숫자 0을 누르세요. \n입력 : ")
            if d_food.isdecimal():
                d_food = int(d_food)
                if d_food ==0:
                    select = input("전체 삭제하시겠습니까? 이 작업은 되돌릴 수 없습니다.\n삭제를 원하면 Y 또는 y / 원치 않으면 다른 버튼을 입력해 주세요 : ")
                    if select == 'Y' or select =='y' : 
                        print('전체 삭제되었습니다.')
                        food_list.clear() 
                    else:continue
                    break
                         
                elif d_food>len(food_list): 
                    print(f'{d_food}번은 목록에 포함되지 않은 숫자입니다.')
                    continue
                else:
                    print(f'{food_list[d_food-1][0]}의 자료가 삭제되었습니다.')
                    del food_list[d_food-1]
                break
            else : 
                print('숫자를 입력하세요.')
                continue
                

    
    elif choice == 4:
        food_kcal = []
        print(f"{'오늘 먹은 음식 보기':-^24}")
        if not len(food_list) : print(f'{"아직 기록된 음식이 없습니다.":^20}')
        else :
            print(f'{"오늘 먹은 음식":-^20}')
            for food in food_list:
                print(f'{food[0]:^24}')
            for i in range(len(food_list)):
                food_kcal.append(food_list[i][1])
            food_kcal = list(map(int,food_kcal))
            calories = sum(food_kcal)
            print(f"총 섭취 칼로리는 {calories}kcal입니다.")
            if rate:
                print(f'기초대사량 대비 {(calories/rate)*100:.2f}% 섭취하였습니다.')
            else : print('기초대사량을 입력하시면 기초대사량 대비 섭취 칼로리의 비율을 볼 수 있습니다.')
            
    

    else: print(f'선택하신 {choice}번에 해당하는 메뉴가 존재하지 않습니다.')