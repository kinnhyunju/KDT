# -----------------------------------------------------------------------------
# 리스트 전용의 함수 즉, 메서드(Method)
# - 리스트의 원소/요소를 제어하기 위한 함수들
# -----------------------------------------------------------------------------
# [메서드 - 요소 추가 메서드 append(데이터)] ------------------------------------
datas = [1,3,5]

# 새로운 데이터 100 추가 : 제일 마지막 원소로 추가
datas.append(100)
print(f'datas 개수 : {len(datas)},{datas}')

datas.append(100)
print(f'datas 개수 : {len(datas)},{datas}')

# [메서드 - 요소 추가 메서드 insert(인덱스, 데이터)] -----------------------------
datas.insert(0,300)
print(f'datas 개수 : {len(datas)},{datas}')

datas.insert(-1,300)
print(f'datas 개수 : {len(datas)},{datas}')

# [실습: 임의의 정수 숫자 10개 저장하는 리스트 생성] -------------------------------
import random
nums = []
while len(nums)<10:
    num = random.randint(0,99)
    nums.append(num)
print(f'nums => {nums}')

# [메서드 - 요소 삭제 메서드 remove(데이터)] -------------------------------------
datas.remove(300)
print(f'datas 개수 : {len(datas)},{datas}')

for cnt in range(datas.count(300)):
    datas.remove(300)
print(f'datas 개수 : {len(datas)},{datas}')
