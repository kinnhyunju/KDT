# -----------------------------------------------------------------
# 함수(Function) 이해 및 활용
# 함수기반 계산기 프로그램
# - 사칙 연산 기능별 함수 생성 => 덧셈, 뺄셈, 곱셈, 나눗셈
# - 2개 정수만 계산
# -----------------------------------------------------------------
def add(n1,n2):
    data = n1+n2
    return data

def minus(n1,n2):
    data = n1-n2
    return data

def multi(n1,n2):
    data = n1*n2
    return data

def div(n1,n2):
    if n2:
        data = n1/n2
    else:
        data = '0으로 나눌 수 없습니다.'
    return data

## 계산기 프로그램 -----------------------------------------------------------------------------
# - 사용자가 종료를 원할때 종료 => 'x', 'X' 입력 시
# - 연산 방식과 숫자 데이터 입력 받기
while True:
    # (1) 입력 받기
    req=input('연산(+, -, *, /) 방식과 정수 2개 입력(예:+ 10 2) : ')
    # (2) 종료 조건 검사
    if req == 'x' or req == 'X': 
        print('계산기를 종료합니다.')
        break
    # (3) 입력의 연산방식과 데이터 추출
    op,num1,num2 = req.split()
    num1 = int(num1)
    num2 = int(num2)
    if op == '+':
        print(f'{num1}+{num2}={add(num1,num2)}')
    elif op == '-':
        print(f'{num1}-{num2}={add(num1,num2)}')
    elif op == '*':
        print(f'{num1}*{num2}={add(num1,num2)}')
    elif op == '/':
        print(f'{num1}/{num2}={add(num1,num2)}')
    else: print(f'{op}는 지원되지 않는 연산입니다.')