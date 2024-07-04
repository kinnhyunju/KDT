# [1] 구구단 for문 1개 사용
data = range(0,81)
for d in data:
    dan = (d//9)+1
    num = (d%9)+1
    if dan>=2:
        print(f'{dan} * {num} = {dan*num}')
    
    if num == 9 : 
        print('-'*60)

# data = range(9,90)
# for d in data:
#     dan = (d//9)+1
#     num = (d%9)+1
#     if dan<=9:
#         print(f'{dan} * {num} = {dan*num}')
    
#     if num ==9 : 
#         print('-'*20)
    

# [2] 2~5단까지 옆으로, 6~9단은 다음 줄로
dan = range(2,6)
num = range(1,10)
for n in num :
    for d in dan:
        print(f'{d} * {n} = {d*n:>2}',end='\t')
        if d==5:
            print()
print('-'*60)
dan = range(6,10)
num = range(1,10)
for n in num :
    for d in dan:
        print(f'{d} * {n} = {d*n:>2}',end='\t')
        if d==9:
            print()

# dan = range(2,10)
# num = range(1,10)
# for n in num :
#     for d in dan:
#         print(f'{d} * {n} = {d*n:>2}',end='\t')
#         if d==9:
#             print()

# p.202~203 ----------------------------------------------------------------------------
# 연습 문제
i=2
j=5
while i<=32 or j>=1:
    print(i,j)
    i=i+i
    j=j-1

# 심사문제
money = int(input())-1350
while money>=0:
    print(money)
    money = money-1350

# p.211~212 ----------------------------------------------------------------------------
# 연습문제
# i=0
# while True:
#     if i>73:
#         break
#     elif i[-1]==3:
#         i = i+1
#     print(i,end=' ')
#     i=i+1
i=0
while True:
    if i>73:
        break
    if i%10 != 3:
        i=i+1
        continue
    print(i,end=' ')
    i=i+1

# 심사문제
start, stop = map(int,(input().split()))
i=start

while True:
    if i>stop:break
    if i%10 == 3:
        i=i+1
        continue
    print(i,end=' ')
    i=i+1

# p.218~219
# 연습문제
for i in range(5):
    for j in range(5):
        if i<=j:
            print('*',end='')
        else:
            print(' ',end='')
    print()

# 심사문제
num = int(input())
for i in range(num):
    for j in range(num):
        if i>=j:
            print('*',end='')
    print()

# p.225~p.226
# 연습문제
for i in range (1, 101):
    if i%22==0:                 # if i%2==0 and i%11==0 : 
        print('FizzBuzz')
    elif i%2==0:
        print('Fizz')
    elif i%11==0 :
        print('Buzz')
    else:
        print(i)

# 심사문제
num = input().split()
num1 = int(num[0])
num2 = int(num[1])
for n in range(num1,num2+1):
    if n%35==0:                 # if i%5==0 and i%7==0 : 
        print('FizzBuzz')
    elif n%5==0:
        print('Fizz')
    elif n%7==0 :
        print('Buzz')
    else:
        print(n)