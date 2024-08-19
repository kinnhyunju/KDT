# p.100~101
# 연습문제
s='''Python is a prgramming language that lets you work quickly
and
intergrate systems more effectively.'''
print(s)
# 심사문제
s = ''''Python' is a "prgramming language"
that lets you work quickly
and
intergrate systems more effectively.'''
print(s)

# p.108~109
# 연습문제
a = list(range(5,-10,-2))
print(a)
# 심사문제
num=int(input())
print(tuple(range(-10,10,num)))

# p.140~142
# 연습문제1
year = [2011,2012,2013,2014,2015,2016,2017,2018]
population = [10249679,10195318,10143645,10103233,10022181,9930616,9857426,9838892]
print(year[-3:])
print(population[-3:])
# 연습문제2
n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2])
# 심사문제1
x=input().split()
del x[-5:]
print(x)

# 심사문제2
data1 = input()[1::2]
data2 = input()[::2]
print(data1+data2)
