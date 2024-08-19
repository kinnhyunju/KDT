# 22.1.2
a = [10,20,30]
a.append(500)
print(a,len(a),'개')        # [10, 20, 30, 500] 4 개

a=[]
a.append(10)
print(a)

# 22.1.3
a = [10,20,30]
a.append([500,600])
print(a,len(a),'개')        # [10, 20, 30, [500, 600]] 4 개

# 22.1.4
a = [10,20,30]
a.extend([500,600])
print(a,len(a),'개')        # [10, 20, 30, 500, 600] 5 개

# 22.1.5
a = [10,20,30]
a.insert(2,500)
print(a,len(a),'개')        # [10, 20, 500, 30] 4 개

a = [10,20,30]
a.insert(0,500)
print(a,len(a),'개')        # [500, 10, 20, 30] 4 개

a = [10,20,30]
a.insert(len(a),500)
print(a,len(a),'개')        #[10, 20, 30, 500] 4 개     a.append(500)과 같음

a = [10,20,30]
a.insert(1,[500,600])
print(a,len(a),'개')        # [10, [500, 600], 20, 30] 4 개

a = [10,20,30]
a[1:1] = [500,600]
print(a,len(a),'개')        # [10, 500, 600, 20, 30] 5 개       a[인덱스:인덱스]일때 주어진 숫자에 맞는 인덱스로 값 추가됨

# 22.1.7
a=[10,20,30]
a.pop()
print(a,len(a),'개')        # [10, 20] 2 개

a=[10,20,30]
a.pop(1)
print(a,len(a),'개')        # [10, 30] 2 개         a.pop(1) 대신 'del a[1]'로 사용 가능

# 22.1.8
a = [10,20,30,20]
print(a,len(a),'개')        # [10, 20, 30, 20] 4 개
a.remove(20)
print(a,len(a),'개')        # [10, 30, 20] 3 개
## 리스트로 스택과 큐 만들기 - deque
from collections import deque
a = deque([10,20,30])
print(a)
a.append(500)
print(a)
print(a.popleft())
print(list(a))

# 22.1.12
a=[10,20,30,15,20,40]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

#22.3.2
a=[38,21,53,62,19]
for index, value in enumerate(a):
    print(index,value)
print()
# 인덱스를 1부터 정하고 싶을때
# [방법1]
a=[38,21,53,62,19]
for index, value in enumerate(a):
    print(index+1,value)                        # 출력할 index에 1 더하기
print()
# [방법2]
for index, value in enumerate(a,start=1):       # enumerate 시작 숫자를 지정하기 => enumerate(a,1) 로 줄여 쓸 수 있음
    print(index,value)

# 22.3.3
a=[38,21,53,62,19]
i=0
while i<len(a):
    print(a[i])
    i=i+1
print()

# 22.4.1
# 반복문 사용해서 최댓값, 최솟값 출력
a=[38,21,53,62,19]
smallest = a[0]
for i in a:
    if i<smallest:
        smallest= i
print(smallest)
a=[38,21,53,62,19]
largest = a[0]
for i in a:
    if i>largest:
        largest= i
print(largest)
# sort() 메서드 사용해서 최댓값, 최솟값 출력
a=[38,21,53,62,19]
a.sort()
print(a[0],a[-1])
# min(), max() 함수 사용
a=[38,21,53,62,19]
print(min(a), max(a))

# 22.4.2
# 반복문 사용해서 요소의 합계 구하기
a = [10,10,10,10,10]
x = 0
for i in a:
    x=x+i
print(x)
# sum()함수 사용해서 요소의 합계 구하기
a=[10,10,10,10,10]
print(sum(a))

# 22.5.1
a=[i for i in range(10) if not i%2]
print(a)

b=[i+5 for i in range(10) if i%2]
print(b)

# 22.5.2
a=[i*j for j in range(2,10) for i in range(1,10)]
print(a)
a=[i*j for j in range(2,10) 
       for i in range(1,10)]
print(a)

# #22.6.1
# nums = map(int,input().split())
# print(list(nums))               # 그냥 대괄호 안에 넣으면 [<map object at 0x00000190D9030FA0>] 이렇게 나오기 때문에 list() 안에 넣어줘야함 [num1, num2]로 나옴
# a,b=map(int,input().split())
# print(a,b, type(a),type(b))

# 22.7.1
a=38,21,53,62,19,53
print(a.index(53))

# 22.7.3
a=38,21,53,62,19,53
for i in a:
    print(i,end=' ')

# 22.7.4
a = tuple(i for i in range(10) if not i%2)
print(a)
# a = (i for i in range(10) if not i%2) => 소괄호안에 넣어서 만들면 튜플이 아니라 제너레이터가 됨!
# => tuple() 형식으로 생성하기

# 22.7.5
a=(1.2,2.5,3.7,4.6)
a=tuple(map(int,a))
print(a)

# 25.1.2
x={'a':10, 'b':20, 'c':30, 'd':40}
x.setdefault('e')
print(x)
x.setdefault('f',100)
print(x)

# 25.1.3
x={'a':10, 'b':20, 'c':30, 'd':40}
x.update(a=90)
print(x)
x.update(e=50)
print(x)
x.update(a=900,f=60)
print(x)

y={1:'one',2:'two'}
y.update({1:'ONE',3:'THREE'})
print(y)

y.update(zip([1,2],['one','two']))
print(y)

# 25.1.4
x={'a':10, 'b':20, 'c':30, 'd':40}
print(x.pop('a'))                       # pop() 대신 del 사용 가능 => del x['a']
print(x)
print(x.pop('z',0))
print(x)

# 25.1.7
x={'a':10, 'b':20, 'c':30, 'd':40}
print(x.get('a'))
print(x.get('z',0))

# 25.1.8
x={'a':10, 'b':20, 'c':30, 'd':40}
print(x.items(),x.keys(),x.values(),sep='\n')

# 25.1.9
x = {'a':0,'b':0,'c':0,'d':0}
from collections import defaultdict
y=defaultdict(lambda:'a')
print(y[8])

# 25.2
x={'a':10, 'b':20, 'c':30, 'd':40}
for key, value in x.items():
    print(key,value)