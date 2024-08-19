# -----------------------------------------------------------------
# 함수(Function) 이해 및 활용
# 함수기반 계산기 프로그램
# - 사칙 연산 기능별 함수 생성 => 덧셈, 뺄셈, 곱셈, 나눗셈
# - 2개 정수만 계산
# -----------------------------------------------------------------
def add(n1,n2): return n1+n2

def minus(n1,n2): return n1-n2

def multi(n1,n2): return n1*n2

def div(n1,n2): return n1/n2 if n2 else'0으로 나눌 수 없습니다.'

# 메뉴 출력 함수 ----------------------------------------------------
# 함수 기능 : 입력 받은 데이터가 유효한 데이터인지 검사하는 함수
# 함수 이름 : check_data
# 매개 변수 : str데이터(예:'10 3'), 데이터 수
# 함수 결과 : True False
# -----------------------------------------------------------------
def check_data(data,num):
    # 입력된 str 데이터 리스트로 변환
    data= data.split()
    # 갯수 체크
    if len(data)==num :
        # 숫자인지 체크
        isOK = True
        for d in data:
            if not d.isdecimal() : 
                isOK=False
                break
        return isOK
    else : return False


# 메뉴 출력 함수 ----------------------------------------------------
# 함수 기능 : 계산기 메뉴를 출력하는 함수
# 함수 이름 : print_menu
# 매개 변수 : 없음
# 함수 결과 : 없음
# -----------------------------------------------------------------
def print_menu():
    print(f"{'*':*^16}")
    print(f'{"*** 계 산 기 ***"}')
    print(f"{'*':*^16}")
    print(f'{"* 1. 덧    셈  *"}')
    print(f'{"* 2. 뺄    셈  *"}')
    print(f'{"* 3. 곱    셈  *"}')
    print(f'{"* 4. 나 눗 셈  *"}')
    print(f'{"* 5. 종    료  *"}')
    print(f"{'*':*^16}")


# -----------------------------------------------------------------
# 함수 기능 : 연산 수행 후 결과를 반환하는 함수
# 함수 이름 : calc
# 매개 변수 : 함수명, str 숫자 2개, str 연산자 기호

# 함수 결과 : 없음
# -----------------------------------------------------------------
def calc(func, op) : 
    # num1, num2 = input("정수 2개 (예:10 2):")
    # num1 = int(num1)
    # num2 = int(num2)
    data=input("정수 2개(예: 10 2): ")
    if check_data(data,2):
        data = data.split()
        print(f'결과:{data[0]}{op}{data[1]}={func(int(data[0]),int(data[1]))}')
    else:
        print(f'{data} : 올바른 데이터가 아닙니다.')


## 계산기 프로그램 --------------------------------------------------
# - 사용자에게 원하는 계산을 선택하는 메뉴를 출력
# - 종료 메뉴 선택 시 프로그램 종료
# => 반복 ---> 무한반복 : while 
# -----------------------------------------------------------------
while True:
    # 메뉴 출력
    print_menu()

    # 메뉴 선택 요청
    choice = input("메뉴 선택:")
    if choice.isdecimal():
        choice = int(choice)
    else:
        print('0~9 사이 숫자만 입력하세요.')
        continue
    # 종료 조건 처리
    if choice == 5:
        print('프로그램을 종료합니다.')
        break    
    elif choice == 1:
        print('덧셈')
        calc(add,'+')
    elif choice == 2:
        print('뺄셈')
        calc(minus,'-')

    elif choice == 3:
        print('곱셈')
        calc(multi,'*')
    elif choice == 4:
        print('나눗셈')
        calc(div,'/')
    else:
        print('선택된 메뉴는 없습니다.')