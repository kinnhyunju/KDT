# --------------------------------------------------------------------------------------------
# 함수와 변수 - 전역 변수
# --------------------------------------------------------------------------------------------
## 전역변수 ----------------------------------------------------------------------------------
persons=["Hong"]
gender = {'h':'남자'}
year=2024

## 사용자 정의 함수 ---------------------------------------------------------------------------
def add_person(name):
    global year
    year += 1
    persons.append(name)
    gender[name] = '여'

def remove_person(name):
    persons.remove(name)
    gender.pop(name)

## 실행 즉, 함수 호출 -------------------------------------------------------------------------
print(f'persons => {persons}')
print(f'gender => {gender}')
add_person('Park')
print(f'persons => {persons}')
print(f'gender => {gender}')

remove_person('Park')
print(f'persons => {persons}')
print(f'gender => {gender}')

# collection 타입 데이터는 글로벌(전역)변수 선언 하지 않아도 자료 수정됨 --> 껍데기는 그대로~