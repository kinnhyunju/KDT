# ------------------------------------------------------------------------------------
# Dict 자료형 살펴보기
# - 연산자와 내장 함수
# ------------------------------------------------------------------------------------
person ={'name':'홍길동', 'age':20, 'job':'학생'}
dog = {'kind':'푸들','weight':'5kg','color':'갈색','gender':'남','age':3}
jumsu = {'국어':90, '수학':178, '체육':100}

## [연산자] --------------------------------------------------------------------------
# 산술 연산 X
# person+dog

# 멤버연산자 : in, not in
#     key
print('name' in dog)
print('name' in person)

#     value : dict 타입에서는 key만 멤버 연산자로 확인 가능
# print('푸들' in dog)
# print(20 in person)

# value 추출
print('푸들' in dog.values())
print(20 in person.values())

## [내장함수] --------------------------------------------------------------------------
# - 원소/요소 개수 확인 : len()
print(f'dog의 요소 개수 : {len(dog)}개')
print(f'person의 요소 개수 : {len(person)}개')

# - 원소/요소 정렬 : sorted()
# - 키만 정렬
print(f'dog 오름차순 정렬 : {sorted(dog)}')
print(f'dog 내림차순 정렬 : {sorted(dog,reverse=True)}')

# print(f'dog 오름차순 정렬 : {sorted(dog.values())}')  ERROR
## - 동일한 타입에서 정렬 가능함 -----------------------------------------
print(f'jumsu 키 오름차순 정렬 : {sorted(jumsu)}')
print(f'jumsu 값 오름차순 정렬 : {sorted(jumsu.values())}')

print(f'jumsu 값 오름차순 정렬 : {sorted(jumsu.items())}')
print(f'jumsu 값 오름차순 정렬 : {sorted(jumsu.items(),key=lambda x:x[1])}')