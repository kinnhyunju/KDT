# ---------------------------------------------------------------------------------------------
# 사용자 정의 함수
# ---------------------------------------------------------------------------------------------
# 덧셈, 뺄셈, 곱셈, 나눗셈 함수를 각각 만들기
# - 매개변수 : 정수2개, num1,num2
# - 함수 결과 : 연산 결과 반환
# ---------------------------------------------------------------------------------------------
def plus(num1,num2):
    return num1+num2

def minus(num1,num2):
    return num1-num2

def multi(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2 if num2 else '0으로 나눌 수 없음'

# ---------------------------------------------------------------------------------------------
# 함수 기능 : 입력 데이터가 유효한 데이터인지 검사해주는 기능
# 함수 이름 : check_data
# 매개 변수 : 문자열데이터, 데이터갯수 data, count, sep = ' '
# 함수 결과 : 유효 여부 True/False
# ---------------------------------------------------------------------------------------------
def check_data(data, count, sep=' ') :
    # 데이터 여부
    if len(data):
        # 데이터 분리 후 갯수 체크
        data2 = data.split(sep)
        return True if count == len(data2) else False
    else:
        return False
    
print(check_data('+ 10 3',3))
print(check_data('+ 10 3 4',3))
print(check_data('+ 10',3))
print(check_data('+,10,3',3,sep=','))

# [실습] 사용자로부터 연산자, 숫자1, 숫자2를 입력 받아서 연산 결과를 출력해주세요
# input("연산자","숫자1", "숫자2 : ").split(', ')
cal,n1,n2 = (input("연산자 숫자1 숫자2 입력(예 : + 10 2): ")).split()
n1 = int(n1)
n2 = int(n2)
if cal == '+': print(plus(n1,n2))
elif cal == '-': print(minus(n1,n2))
elif cal == '*': print(multi(n1,n2))
else : print(div(n1,n2))

# 해설 (연산자 확인 -> 정수인지 확인        / + 자료가 있는지 없는지도 확인해야 완벽함)
if cal not in ['+','-','*','/']:
    print(f'{cal} : 잘못된 연산자입니다')
else :
    if n1.isdecimal() and n2.isdecimal() :
        n1 = int(n1)
        n2 = int(n2)
        result = 0
        if cal == '+':result = plus(n1,n2)
        elif cal == '-': result = minus(n1,n2)
        elif cal == '*': result = multi(n1,n2)
        else : result = div(n1,n2)
        print(f'{n1}{cal}{n2}={result}')
    else:
        print('정수만 입력 가능합니다.')