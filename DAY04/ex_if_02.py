# -----------------------------------------------------------------------------------------
# [실습] 숫자를 입력 받아서 음이 아닌 정수와 음수 구분하기
## - 출력 : 숫자 -5는 음수입니다.
# -----------------------------------------------------------------------------------------
num = int(input("정수를 입력하세요 : "))

if num >=0:
    print(f'숫자 {num} : 음이 아닌 정수입니다.')
else:
    print(f'숫자 {num} : 음수입니다.')

# -----------------------------------------------------------------------------------------
# [실습] 점수를 입력 받아서 합격과 불합격 출력
# - 합격 : 60점 이상
# -----------------------------------------------------------------------------------------
jumsu = int(input("점수를 입력하세요 : "))
if jumsu>=60:
    print(f'{jumsu}점으로 합격입니다.')
else:
    print(f'{jumsu}점으로 불합격입니다.')

# -----------------------------------------------------------------------------------------
# [실습] 점수를 입력 받아서 학점 출력
# - 학점 : A, B, C, D, F
# -----------------------------------------------------------------------------------------
grade = int(input("점수를 입력하세요 : "))
if grade>=90:
    print(f'{grade}점 : A학점입니다.')
elif grade>=80 and grade<90:
    print(f'{grade}점 : B학점입니다.')
elif grade>=70 and grade<80:
    print(f'{grade}점 : C학점입니다.')
elif grade>=60 and grade<70:
    print(f'{grade}점 : D학점입니다.')
else:
    print(f'{grade}점 : F학점입니다.')