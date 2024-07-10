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

# 식단 목록, 기초대사량 초기값 기록
## 음식 이름을 키, 칼로리를 값으로 만들어 딕셔너리로 만들려고 했으나 중복으로 기록할 수 없어 리스트로 설정
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
        save = input('''식단 일기를 종료합니다. 파일로 저장하시겠습니까?
저장을 원하시면 Y 또는 y 를 입력하고, 원하지 않으면 그 외 버튼을 입력해주세요.
입력 : ''')
    # 파일 저장 : Yes 일때
        if save == 'Y' or save =='y':
            filename = '식단일기.txt'
            f = open(filename,mode='a',encoding='utf-8')
            print(f'나의 기초대사량     : {round(rate)}kcal',file=f)
            food_kcal = []
            if not len(food_list) : calories = 0
            else :
                for i in range(len(food_list)):
                    food_kcal.append(food_list[i][1])
                food_kcal = list(map(int,food_kcal))
                calories = sum(food_kcal)
            print(f'오늘 총 섭취 칼로리 : {calories}kcal',file=f,end='\n\n')
            f.close()
            print('파일이 저장되었습니다.')
        print('식단 일기를 종료합니다.')
        break



    elif choice == 1:
        # 기초대사량 기록. 들어올 때마다 업데이트 되도록 0으로 설정
        rate = 0
        while True:
            print(f"{'기초대사량 계산':-^24}")
            gender = input("성별을 선택하세요. (뒤로가기는 B 또는 b를 입력하세요.)\n    1. 남     2. 여\n선택 : ")
            # 뒤로가기 눌렀을 때 페이지 나가도록 설정
            if gender == "B" or gender == "b": break
            # B/b를 제외한 문자 또는 숫자를 눌렀을 때 결과값
            else :
                if gender.isdecimal():
                    gender = int(gender)
                else:
                    print('숫자를 입력해주세요.')
                    continue
                # 남 또는 여를 선택했을 때
                if gender == 1:
                    while True:
                        info = input("신장(cm), 체중(kg), 나이(만)를 입력하세요 (예 : 130 20 10)\n입력 : ").split()
                        if len(info) ==3:
                            if info[0].isdecimal() and info[1].isdecimal() and info[2].isdecimal():
                                height = int(info[0])
                                weight = int(info[1])
                                age = int(info[2])
                                rate = 66.47 + (13.75 * weight) + (5* height) - (6.76 * age)
                                print(f"기초대사량은 {round(rate)}kcal입니다.")
                                break
                            # 값에 숫자 외에 문자가 입력 됐을 때
                            else: 
                                print('숫자만 입력하세요')
                            continue
                        # 3개의 데이터가 들어오지 않았을 때
                        else: 
                            print('예시에 맞게 신장(cm), 체중(kg), 나이(만)를 다시 입력하세요.\n')
                        continue
                    break              
                elif gender == 2:
                    while True:
                        info = input("신장(cm), 체중(kg), 나이(만)를 입력하세요 (예 : 130 20 10)\n입력 : ").split()
                        if len(info) ==3:
                            if info[0].isdecimal() and info[1].isdecimal() and info[2].isdecimal():
                                height = int(info[0])
                                weight = int(info[1])
                                age = int(info[2])
                                # 기초 대사량 기록
                                rate = 655.1 + (9.56 * weight) + (1.85 *height) - (4.68 * age)
                                print(f"기초대사량은 {round(rate)}kcal입니다.")
                                break
                            else: 
                                print('숫자만 입력하세요')
                            continue
                        else: 
                            print('예시에 맞게 신장(cm), 체중(kg), 나이(만)를 다시 입력하세요.\n')
                        continue
                    break 
                # 성별 선택에서 숫자는 넣었으나 1(남성)번 또는 2(여성)번이 아닐 때
                else: 
                    print(f"{gender}번은 해당되지 않습니다.성별을 다시 선택해 주세요.")
                    continue

    

    elif choice == 2:
        print(f"{'오늘 먹은 음식 추가':-^24}")
        key = input("오늘 먹은 음식을 입력하세요. (뒤로가기는 B 또는 b를 입력하세요.)\n입력 : ")
        if key =='B' or key =='b' : continue
        else:
            while True:
                value = input(f"{key}의 칼로리를 입력하세요 : ")
                # 칼로리를 숫자로 입력했다면 음식 리스트트에 음식 이름과 칼로리를 리스트 형식으로 추가
                # 음식 리스트 = [   [음식 이름1, 칼로리1] , [음식이름2, 칼로리2]   ] 
                if value.isdecimal():
                    food_list.append([key,value])
                    break
                else :
                    print("칼로리는 숫자로만 입력해야 합니다.\n")
                    continue



    elif choice == 3:
        print(f"{'오늘 먹은 음식 삭제':-^24}")
        print(f'{"오늘 먹은 음식":-^24}')
        while True:
            for i in range(len(food_list)):
                # 삭제할 때 번호를 입력받아서 삭제할 예정. 리스트 인덱스에 1을 더해서 번호 받기
                print(f'{i+1:>5}. {food_list[i][0]}    {food_list[i][1]}kcal')
            d_food = input("삭제할 음식의 번호를 입력하세요. (뒤로가기는 B 또는 b를 입력하세요.)\n전체 삭제를 원하면 숫자 0을 입력하세요. \n번호 입력 : ")
            if d_food.isdecimal():
                d_food = int(d_food)
                # 0을 누르면 확인 질문 후 Y 또는 y를 입력하면 전체 삭제 실행
                if d_food ==0:
                    select = input("전체 삭제하시겠습니까? 이 작업은 되돌릴 수 없습니다.\n삭제를 원하면 Y 또는 y / 원치 않으면 다른 버튼을 입력해 주세요 : ")
                    if select == 'Y' or select =='y' : 
                        print('전체 삭제되었습니다.')
                        food_list.clear() 
                    else:continue
                # 목록에 포함되지 않은 숫자를 입력하면 다시 입력하도록 출력         
                elif d_food>len(food_list): 
                    print(f'{d_food}번은 목록에 포함되지 않은 숫자입니다.')
                    continue
                # 목록 내에 있는 숫자를 입력하면 '음식이름'의 자료 삭제
                else:
                    print(f'{food_list[d_food-1][0]}의 자료가 삭제되었습니다.')
                    del food_list[d_food-1]
                break
            # 뒤로 가기를 누르면 첫번째 창으로 다시 돌아감
            elif d_food =='B' or d_food =='b' : break
            # 숫자가 아니라 문자를 입력했을 때 출력
            else:
                print('숫자를 입력하세요.')
                continue
                

    
    elif choice == 4:
        food_kcal = []
        print(f"{'오늘 먹은 음식 보기':-^24}")
        # 먹은 음식 기록되지 않았을 때 출력 내용
        if not len(food_list) : print(f'{"아직 기록된 음식이 없습니다.":^20}')
        # 기록했다면 먹은 음식과 음식 칼로리 합산 출력
        else :
            print(f'{"오늘 먹은 음식":-^20}')
            for food in food_list:
                print(f'{food[0]:^24}')
            for i in range(len(food_list)):
                food_kcal.append(food_list[i][1])
            food_kcal = list(map(int,food_kcal))
            calories = sum(food_kcal)
            print(f"총 섭취 칼로리는 {calories}kcal입니다.")
            # 앞에서 기초대사량 계산을 실행하면 기초대사량 대비 섭취 칼로리 비율 출력 / 실행 안하면 하게끔 출력
            if rate:
                print(f'기초대사량 대비 {(calories/rate)*100:.2f}% 섭취하였습니다.')
            else : print('기초대사량을 입력하시면 기초대사량 대비 섭취 칼로리의 비율을 볼 수 있습니다.')
            
    

    else: print(f'선택하신 {choice}번에 해당하는 메뉴가 존재하지 않습니다.')