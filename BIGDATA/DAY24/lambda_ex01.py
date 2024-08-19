# -----------------------------------------------------------------------
# key 매개변수
# -----------------------------------------------------------------------
msg = "The health know not of their health, but only the sick"
sorted_list = sorted(msg.split(), key = str.lower)
print(sorted_list)

# -------------------------------------------------
# 문자열의 길이를 기준으로 내림차순 정렬
msg = "The health know not of their health, but only the sick"
descending_sorted_list = sorted(msg.split(), key= len, reverse=True)
print(descending_sorted_list)

# -------------------------------------------------
# 여러 항목을 가지는 리스트 정렬
students = [('Alice', 3.9, 20160303),('Bob', 3.0, 20160302),('Charlie', 4.3, 20160301)]

print('-'*50)
print('sorted key 입력 없음')
print(sorted(students))
print('-'*50)

# -------------------------------------------------
# 학번(students[2])을 기준으로 오름차순 정렬
print('학번(students[2])을 기준으로 오름차순 정렬')
sorted_students1 = sorted(students, key= lambda s : s[2])
print(sorted_students1)

# 학점(students[1])을 기준으로 내림차순 정렬
print('-'*50)
sorted_students2 = sorted(students, key= lambda s : s[1], reverse=True)
print(sorted_students2)
print('-'*50)

# -------------------------------------------------
# 객체 리스트의 정렬 기준 설정
class Student:
    def __init__(self,name,grade,number):
        self.name = name
        self.grade = grade
        self.number = number

    def __repr__(self):
        return f'({self.name}, {self.grade}, {self.number})'
    
# Students 객체 리스트 생성
students = [Student('홍길동', 3.9, 20240303),
            Student('김유신', 3.0, 20240302),
            Student('박문수', 4.3, 20240301)]

print(students[0])

sorted_list = sorted(students, key= lambda s: s.name)
print(sorted_list)

# -------------------------------------------------
# 딕셔너리에 lambda 적용
import pandas as pd
addr_aliases= {'경기':'경기도', '경남':'경상남도', '경북':'경상북도', '충북':'충청북도', 
                                  '서울시':'서울특별시', '부산특별시':'부산광역시', '대전시':'대전광역시',
                                  '부산시':'부산광역시', '충남':'충청남도', '전남':'전라남도', '전북':'전라북도'}

print(addr_aliases.get('경기'))
print(addr_aliases.get('대전')) # None을리턴
print(addr_aliases.get('부산')) # ‘부산’ key는없음
print(addr_aliases.get('부산', '부산광역시')) # key에‘부산’이없으면‘부산광역시’리턴