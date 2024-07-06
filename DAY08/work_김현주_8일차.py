# # p. 303~306
# # [24.4] 연습문제
# path = 'C: \\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
# start = path.rfind('\\')
# filename = path[start+1:]
# print(filename)

# # [24.5] 심사문제
# msg = input().split()
# i = 0
# for m in msg:
#     if m.strip(',.') == 'the': i=i+1
# print(i)

# # [24.6] 심사문제
# nums = input().split(';')
# price = list(map(int,nums))
# price.sort(reverse=True)
# for p in price:
#     print('{0:>9,}'.format(p))          # 콤마가 없었으면 rjust로 쓸 수 있을 듯!

# # p.384~385
# # [29.7] 연습문제
# x=10
# y=3

# def get_quotient_remainder(a,b):
#     return a//b, a%b

# quotient,remainder = get_quotient_remainder(x,y)
# print('몫:{0}, 나머지:{1}'.format(quotient,remainder))

# # [29.8] 심사문제
# x,y = map(int,input().split())
# def calc(n1,n2):
#     return n1+n2, n1-n2, n1*n2, n1/n2

# a, s, m, d = calc(x,y)
# print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a,s,m,d))

# # p.397~398
# # [30.6] 연습문제
# korean, english, mathematics, science = 100,86,81,91
# def get_max_score(*args):
#     return max(args)            # 반환값은 max(*args) 에서 * 빼기

# max_score = get_max_score (korean, english, mathematics, science)
# print('높은 점수:', max_score)
# max_score = get_max_score(english, science)
# print('높은 점수:', max_score)
    
# # [30.7] 심사문제
# korean, english, mathematics, science = map(int,input().split())
# score = {'korean':korean, 'english' : english, 'mathematics' : mathematics, 'science' : science}
# def get_min_max_score(*num):
#         return min(num), max(num)

# def get_average(**score):
#     jumsu = 0
#     for i in score.values():
#         jumsu = jumsu+ i
#     return jumsu/len(score)    

# min_score, max_score = get_min_max_score(korean, english, mathematics, science)
# average_score = get_average(korean=korean, english=english,mathematics=mathematics,science=science)
# print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))
# min_score, max_score = get_min_max_score(english, science)
# average_score = get_average(english=english, science=science)
# print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))
# # ---------------------------------------------------------------------------------------------------------------------------
# # 24.1.2 - translate
# change = str.maketrans('aeiou','12345')     # 키, 값으로 묶인 딕셔너리 생성 (아스키코드로 변환되어 저장)
# print(change)
# print('apple'.translate(change))

# # 24.1.4
# fruit = ' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
# print(fruit)
# fruit = '-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
# print(fruit)

# # 24.1.12
# msg = ', python. '
# print(f"msg.strip(',. ') :{msg.strip(',. ')}/ {len(msg)}개 => {len(msg.strip(',. '))}개")
# # 구두점 삭제
# import string
# print(msg.strip(string.punctuation))
# # 공백까지 지우고 싶을때 : 
# print(msg.strip(string.punctuation+' '))

# # 24.1.13 / 24.1.14 / 24.1.15
# print('python'.ljust(10))
# print('python'.rjust(10))
# print('python'.center(10))

# # 24.1.17
# print('35'.zfill(6))

# # 24.2.1
# print('I am %s'%'james')

# # 24.2.3
# print('%.3f'%2.3)

# # 24.2.4
# print('%10s'%'python')
# # 자릿수가 다른 숫자 출력하기
# print('I am %3d years old.'%20)
# print('%10d'%150)
# print('%10d'%1500)
# print('%10.2f'%2.3)         # 실수 정렬 '%(문자길이) . (소수점자리)f' % 소수
# print('%10.2f'%2000.3)
# print('%-10s'%'python')     # 문자열 왼쪽 정렬
# print('%-10.2f'%2.3)        
# print('%-10.2f'%2000.3)

# # 24.2.5
# print('Today is %s %d'%('April',3))     # 변수 개수 맞추기, 괄호로 묶어 콤마로 구분

# # 24.2.7
# print('Hello, {0} {2} {1}'.format('python','Script','3.6')) 
# # 인덱스를 생략하면 format에 지정한 순서대로 값이 들어가며 중괄호 개수만큼 format()안에 값의 개수를 맞춰 넣어야함
# # 인덱스 대신 이름에 해당하는 값을 넣을 수 있음 => 딕셔너리 키랑 비슷

# # 24.2.12
# # '{인덱스:<길이}'.format(값)
# print('{0:<10}'.format('python'))
# print('{0:>10}'.format('python'))
# print('{:>10}'.format('python'))                # 인덱스를 사용하지 않는다면 숫자 생략 가능, 값이 하나만 있을때 인덱스는 항상 0
# print('{1:>10}'.format('goodluck','hello'))     # 정렬할 데이터의 인덱스를 지정한뒤 정렬방향, 자릿수 지정

# # 24.2.13
# # 정수 표현 : '{인덱스:빈칸에넣을문자/자릿수/d}'.format(정수값)
# # 실수 표현 : '{인덱스:빈칸에넣을문자/자릿수 . 소수자릿수/f}'.format(실수값)
# # 단, 실수 표현의 자릿수는 정수의 개수가 아니라 소수점이하 자리까지 포함한 총 데이터의 자릿수를 말함

# # 24.2.14
# # '{인덱스:빈칸에넣을문자/정렬/자릿수 . 소수자리수/자료}'.format(값)
# # 예시 : 12.3을 소수점자리 3개, 총 자릿수 8개로 표현, 빈자리는0으로 채우기,오른쪽 정렬
# print('{:0>8.3f}'.format(12.3))
# # 금액에서 천단위로 콤마 넣기
# # 메서드로 콤마 넣을 때 :'{인덱스:,}'.format(숫자)
# # 함수로 콤마 넣을 때 : format(숫자,',')
# # 정렬과 콤마 같이 실행 : '{인덱스/:/정렬/,/}.format(숫자)
 
# # ---------------------------------------------------------------------------------------------------------------------------
# # 29.2
# def add(a,b):
#     """2개의 매개변수(인수)를 더해준 후 출력하는 함수
#     독스트링 연습해보려고 만든 설명입니다,,,
#     파이썬 코딩 스타일 가이드에서는 큰따옴표를 권장합니다"""
#     print(a+b)
# add(3,5)
# help(add)

# # 29.3
# def add(a,b):
#     """2개의 매개변수(인수)를 더해준 후 반환하는 함수
#     독스트링 연습해보려고 만든 설명입니다,,,
#     파이썬 코딩 스타일 가이드에서는 큰따옴표를 권장합니다"""
#     return a+b                  # return 뒤에 값을 지정하지 않으면 None을 반환

# 29.4
def add_sub(a,b):
    return a+b, a-b             # 함수 값을 여러개 반환할때는 값이나 변수를 ,(콤마)로 구분해서 지정 ==> 튜플이 반환됨!
print(add_sub(8,4))             # 함수를 정의할때 리스트가 반환되도록 대괄호로 묶으면 리스트로 반환 가능 / 언패킹으로 변수 여러개에 할당도 가능함 (튜플 특성)   

# 29.5
# 함수는 스택방식으로 호출됨. 후입선출 ==> 함수를 호출하면 스택의 아래쪽으로 추가되며 끝나면 위쪾으로 사라짐

# 30.1.1
# 위치 인수 : 인수를 순서대로 넣는 방식. 인수의 위치가 정해져 있음      ex)print(10,20,30)--> 10 20 30 이 순서대로 출력됨

# 30.1.2
def print_numbers(a,b,c):
    print(a)
    print(b)
    print(c)

x=[10,20,30]
print_numbers(*x)
# 리스트(튜플) 앞에  * 을 붙이면 언패킹이됨. 단, 함수의 매개변수 개수와 리스트의 요소 개수는 같아야함! 아니면 Error

# 30.1.3
def print_numbers(*args):
    for arg in args:
        print(arg)              # 반복문을 사용해서 출력

# 가변인수 함수는 매개변수 앞에 * 을 붙임  ==> 인수의 개수가 가변적이라는 말로 이 경우에 넣은 데이터의 개수만큼 출력됨
# 인수에 데이터 여러개를 직접 넣어도 되고, 리스트나 튜플을 넣어 언패킹할 수 있음

## 정리 : 매개변수에 * 을 붙여주면 가변 인ㅅ누 함수를 만들수 있다. 함수를 호출할 때는 인수를 각각 넣거나 리스트(튜플)언패킹 사용
#           +) 고정인수와 가변인수를 함께 사용할때 항상 고정 매개 변수를 지정하고 가변인수를 지정해야함!!

# 30.2
def personal_info(name, age, address):
    print('이름: ',name)
    print('나이: ',age)
    print('주소: ',address)
# 키워드 인수 : 인수에 이름(키워드)를 붙이는 기능. 키워드=값 형식으로 사용

personal_info(age=30,address='서울시 용산구 이촌동',name='홍길동')
# 키워드 인수 사용시 인수의 숫서를 맞추지 않아도 키워드에 해당하는 값을 할당        예) print()함수에서 sep=' '/ end = '\n'

# 30.3 / 30.4
def personal_info(name, age, address):
    print('이름: ',name)
    print('나이: ',age)
    print('주소: ',address)

x = {'name':'홍길동','age':30,'address':'서울시 용산구 이촌동'}
personal_info(**x)
# 딕셔너리 언패킹 : 함수(**딕셔너리) / 함수의 매개변수 이름과 딕셔너리의 키 이름이 같아야함. 매개변수의 개수와 딕셔너리 키의 개수도 같아야함!
# **을 두번 싸용하는 이유 : 값을 사용하기 위해서는 *을 두번 사용해야함      한번 사용하면 값이 아니라 키를 사용하게 됨

## 고정인수와 가변인수(키워드인수)      를 사용할 때 순서 : 고정인수, 가변인수(키워드인수)
## 위치인수와 키워드인수               를 사용할 때 순서 : 위치인수, 키워드인수
## 고정 매개변수와 위치인수 키워드인수  를 사용할 때 순서 : 고정매개변수, 위치인수, 키워드인수