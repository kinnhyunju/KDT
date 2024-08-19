# -----------------------------------------------------------------------------
# 리스트 전용의 함수 즉, 메서드(Method)
# - 리스트의 원소/요소를 제어하기 위한 함수들
# -----------------------------------------------------------------------------
import random as rad

# [1] 실습 데이터 => 임의의 정수 숫자 10개로 구성된 리스트
datas = [7,3,9,11,5,3,2,3,8,4]

# [메서드 - 요소 인덱스를 반환하는 메서드 index(찾을데이터, 찾기시작할인덱스)] 
# -> 11의 인덱스를 찾기
# -> 왼쪽 >>>> 오른쪽으로 찾기
idx = datas.index(11)
print(f'11의 인덱스 : {idx}')

# -> 데이터 0의 인덱스를 찾기 ==> 존재하지 않는 데이터의 경우 ERROR 발생
if 0 in datas: 
    idx = datas.index(0)
    print(f'0의 인덱스 : {idx}')
else :
    print('0은 존재하지 않는 데이터 입니다.')

# -> 3의 인덱스 찾기
if 3 in datas:
    idx = datas.index(3)
    print(F'첫번째 3의 인덱스 : {idx}')

    idx = datas.index(3,idx+1)
    print(F'두번째 3의 인덱스 : {idx}')

    idx = datas.index(3,idx+1)
    print(F'세번째 3의 인덱스 : {idx}')

# [메서드 - 데이터가 몇개 존재하는지 갯수 파악하는 메서드 count(데이터)] 
datas = [7,3,9,11,5,3,2,3,8,4]
cnt = datas.count(3)
print(f'3의 개수 : {cnt}개')

idx = 0
for i in range(cnt):
    idx = datas.index(3,idx if not i else idx+1)
    print(f'{i+1}번째 3의 인덱스 : {idx}')