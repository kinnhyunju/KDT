# -------------------------------------------------------------------------
# [실습 1] 글자를 입력 받습니다
#          입력 받은 글자의 코드값을 출력합니다.
# -------------------------------------------------------------------------
char = input("글자를 입력하세요(a~z,A~Z) : ")
# if len(char)>0 :
#     if len(char)==1 :
#         if 'a'<=char<='z' or 'A'<=char<='Z':
#             print(f'{char}의 코드값 : {ord(char)}')
#         else:
#             print("알파벳 대문자, 소문자만 가능합니다.")
#     else :
#         print('1개의 문자만 입력해야합니다.')
# else :
#     print('입력된 데이터가 없습니다. 확인하세요')


if len(char)==1 and ('a'<=char<='z' or 'A'<=char<='Z'):
    print(f'{char}의 코드값 : {ord(char)}')
else :
    print('1개의 알파벳 대문자, 소문자만 입력해야합니다.\n입력된 데이터를 확인하세요')

# -------------------------------------------------------------------------
# [실습 2] 점수를 입력 받은 후 학점을 출력합니다.
# - 학졈 : A+, A, A-,B+,B,B-,C+,C,C-,D+,D,D-,F
# A+ : 96~100 / A : 95 / A- : 90~94
# -------------------------------------------------------------------------
grade = int(input("점수를 입력하세요 : "))
hakjum = ''

if grade>=0 and grade<=100:
    if grade>95: hakjum = 'A+'
    elif grade==95 :hakjum = 'A'
    elif grade>=90: hakjum = 'A-'
    elif grade>=85: hakjum = 'B+'
    elif grade==85 :hakjum = 'B'
    elif grade>=80:hakjum = 'B-'
    elif grade>75 :hakjum = 'C+'
    elif grade==75 :hakjum = 'C'
    elif grade>=70 :hakjum = 'C-'
    elif grade>65 :hakjum = 'D+'
    elif grade==65 :hakjum = 'D'
    elif grade>=60 : hakjum = 'D-'
    else:hakjum = 'F'
    print(f'{grade}점의 학점은 {hakjum}입니다.')
else:
    print('0~100까지 숫자만 입력하세요.')