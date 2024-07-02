# 081
*valid_score,score1,score2 = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
print(valid_score)
# 082
_,_,*valid_score = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
print(valid_score)
# 083
_,*valid_score,_ = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
print(valid_score)
# 084
temp = dict() # {}
# 085
icecream = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
# 086
icecream['죠스바']=1200
icecream['월드콘']=1500
# 087
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print(f"메로나 가격 : {ice['메로나']}")
# 088
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice['메로나'] = 1300
print(ice)
# 089
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
del ice['메로나']
print(ice)

# 090
# icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'
# 누가바 키가 존재하지 않고, 키에 맞는 값을 지정해 주지 않아 오류 발생
# 딕셔너리에 없는 키를 사용해서 인덱싱하면 에러가 발생합니다.

# 091
inventory = {'메로나':[300,20],'비비빅':[400,3],'죠스바':[250,100]}

# 092
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print(inventory['메로나'][0],'원')

# 093
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print(inventory['메로나'][1],'개')

# 094
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
inventory['월드콘'] = [500,7]
print(inventory)

# 095
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
name = icecream.keys()
print(name)

# 096
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
price = icecream.values()
print(price)

# 097
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
price = list(icecream.values())
print(sum(price))

# 098
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

# 099
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys,vals))
print(result)

# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))
print(close_table)

# 101
# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가? : Boolean(논리형)

# 102
print(3 == 5)       # False

# 103
print(3 < 5)        # True

# 104
x = 4
print(1 < x < 5)    # True

# 105
print ((3 == 3) and (4 != 3))   # True

# 106
# print(3 => 4)     # 비교 연산자 방향이 틀림 >=

# 107
if 4 < 3:
    print("Hello World")
# 아무것도 출력 안 됨 (False이기 때문)
# 조건을 만족하지 않기 때문에 아무 결과도 출력되지 않습니다.

# 108
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
# Hi, there. => 조건을 만족하지 않기 때문에 else 조건문 출력

# 109
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
# 1/2/4 출력

# 110
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
# 3/5 출력

# 111
msg = input()
print(msg*2)

# 112
num = int(input("숫자를 입력하세요: "))
print(num+10)

# 113
num = int(input())
if num%2==0:
    print('짝수')
else:
    print('홀수')

# 114
num = int(input("입력값: "))
num2 = num+20
if num2<=255:
    print(num+20)
else:
    print (255)

# 115
num = int(input("입력값: "))
num2 = num-20
if num2>=0 and num2<=255:
    print(num-20)
elif num2<0:
    price(0)
else:
    print (255)

# 116
time = input("현재시간 : ")
if time[-2:] == "00":
    print('정각 입니다.')
else:
    print('정각이 아닙니다')

# 117
fruit = ["사과", "포도", "홍시"]
msg = input("좋아하는 과일은? ")
if msg in fruit:
    print("정답입니다")
else:
    print("오답입니다")

# 118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
investment = input("종목명 : ")
if investment in warn_investment_list:
    print('투자 경고 종목입니다')
else : 
    print('투자 경고 종목이 아닙니다.')

# 119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
season = input("제가좋아하는계절은 : ")
if season in fruit:
    print("정답입니다")
else : 
    print("오답입니다")

# 120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
season = input("좋아하는 과일은? ")
if season in fruit.values():
    print("정답입니다")
else : 
    print("오답입니다")

# 121

# 122
score = int(input("score: "))
if score>=81 and score<=100:
    print('grade is A')
elif score>=61 and score<=80:
    print('grade is B')
elif score>=41 and score<=60:
    print('grade is C')
elif score>=21 and score<=40:
    print('grade is D')
else:
    print('grade is E')

# 123
money = input("입력: ").split()
name = money[1]
num = int(money[0])
if name == "달러":
    print(num*1167,'원')
elif name == "엔":
    print(num*1.096,'원')
elif name == "유로":
    print(num*1268,'원')
else:
    print(num*171,'원')

# 124
