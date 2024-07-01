# p.149~150
# 연습문제
camille = {'health': 575.6,
'health_regen': 1.7,
'mana': 338.8,
'mana_regen': 1.63,
'melee': 125,
'attack_damage': 60,
'attack_speed': 0.625,
'armor': 26,
'magic resistance': 32.1,
'movement_speed': 340}
print(camille['health'])
print(camille['movement_speed'])
# 심사문제
keys = input().split()
values = input().split()
datas = dict(zip(keys,values))
print(datas)

# p.164~165
# 연습문제
x = 5
if x!=10:
    print('ok')
# 심사문제
cost = int(input())
coupon = input()
if coupon == 'Cash3000':
    print(cost-3000)
if coupon == 'Cash5000':
    print(cost-5000)

# p. 174~175
# 연습문제
written_test = 75
coding_test = True
if written_test>=80 and coding_test==True:
    print('합격')
else:
    print('불합격')
# 심사문제
jumsu = input().split()
avg = (int(jumsu[0])+int(jumsu[1])+int(jumsu[2])+int(jumsu[3]))/4
if 0<=int(jumsu[0])<=100 and 0<=int(jumsu[1])<=100 and 0<=int(jumsu[2])<=100 and 0<=int(jumsu[3])<=100 :
    if avg>=80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')

# p.180~181
# 연습문제
x = int(input())
if x>=11 and x<=20 :
    print("11~20")
elif x>=21 and x<=30:
    print("21~30")
else:
    print('아무것도 해당하지 않음')
# 심사문제
age = int(input())
balance = 9000
if age>=7 and age<=12:
    balance = balance-650
elif age>=13 and age<=18:
    balance = balance-1050
if age>=19:
    balance = balance-1250
print(balance)