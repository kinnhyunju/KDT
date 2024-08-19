## ------------------------------------------------------------------------------------
## => 한줄로 조건식 축약 : 조건부 표현식
## ------------------------------------------------------------------------------------
## [실습] 임의의 숫자가 5의 배수인지 여부 결과를 출력하세요.
num = 50         # int(input("숫자 입력 : "))
print(f'{num} : 5의 배수입니다.') if not num%5 else print(f'{num} : 5의 배수가 아닙니다.')


## [실습] 문자열을 입력 받아서 문자열의 원소 개수를 저장
## - 단 원소 개수가 0이면 None 저장
## - (1) 입력받기 input()
## - (2) 원소/요소 개수 파악 len()
## - (3) 원소/요소 개수 저장 단, 0인경우 None 저장하기
msg = input("문자 입력 : ")
# result = len(msg) if len(msg) > 0 else None   => 비교연산자 생략 가능
result = len(msg) if len(msg) else None
print(f'{msg}의 원소 개수 : {result}')

## [실습] 연산자(사칙연산자 : +, -, *, /)와 숫자 2개 입력 받기
## - 입력된 연산자에 따라 계산 결과 저장
## - 예) + 10 30      출력 : 13
num = input("사칙연산자 1개와 숫자2개 입력 (예: + 10 30) : ").split()
num1 = int(num[1])
num2 = int(num[2])
cal = num[0]
if cal == '+': result = num1+num2       # 값 저장 꼭!
elif cal == '-': result = num1-num2
elif cal == '*': result = num1*num2
else : result = num1/num2
print ('계산 결과 :',result)