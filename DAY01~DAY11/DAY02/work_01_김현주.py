# p.48~49
print('Hello, world!')      # 퀴즈1
print('Hello, world!')      # 연습문제
print('Python Programming') 
print('Hello, world!')      # 심사문제
print('Hello, world!')

# p.61~62
print(f'10 / 4 = {10/4}')   # 퀴즈1
print(float(10//3))         # 퀴즈2
print(7+(10-5)*2)           # 퀴즈3
# 연습문제
dist = 12
print(f'소음이 가장 심한층 : {int(0.2467*dist*4.159)}')
# 심사문제
AP = 102
print(f'스킬 피해량 : {AP*0.6+225}')

# p.75
# 연습문제
a,b,c = map(int,input().split())
print(a+b+c)
# 심사문제
msg = '50,100,None'
a,b,c = map(str,msg.split(','))
print(a)
print(b)
print(c)

# p.80~81
# 연습문제
year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59
print(year,month,day,sep='/',end=' ')
print(hour,minute,second,sep=':')
# 심사문제
year, month, day, hour, minute, second = input().split()
print(year,month,day,sep='-',end='T')
print(hour,minute,second,sep=':')

# p.94~95
# 연습문제
korean = 92
english = 47
mathematics = 86
science = 81
print( korean>=50 and english>=50 and mathematics>=50 and science>=50)

# 심사문제
korean,english,mathematics,science = map(int, input().split())
print(korean>=90 and english>80 and mathematics>85 and science>=80)
