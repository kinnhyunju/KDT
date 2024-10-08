# ---------------------------------------------------------------------------------------------
# 사용자 정의 함수
# ---------------------------------------------------------------------------------------------
# 목적 : 매개 변수의 개수를 유동적으로 0개~N개까지 가능하도록
# 형태 : def 함수명( *변수명 ) <= 0개~N개 데이터 받을 수 있음
# ---------------------------------------------------------------------------------------------
# 함수 기능: 정수를 덧셈한 후 결과를 반환/리턴해주는 함수
# 함수 이름: add
# 매개 변수: 0개~N개
# 함수 결과: 덧셈 계산
# ---------------------------------------------------------------------------------------------
def add(*nums):
    total = 0
    for n in nums:
        total=total+n
    return total

# 함수 호출 ------------------------------------------------------------------------------------
print(add())
print(add(1,1,1))
print(add(5,6))
print(add(8,9,11,22,55,11,6,7))