# ---------------------------------------------------------------------------------------------
# str 데이터 타입 전용 함수 즉, 메서드 살펴보기
# ---------------------------------------------------------------------------------------------
## [문자열을 구성하는 문자를 검사해주는 메서드] --------------------------------------------------
## - isXXXX() ---> 결과 논리형 True/False
## [1] 알파벳으로 구성된 문자열인지 검사 isalpha()
data = "good"
print(f'{data} ==> {data.isalpha()}')

## [2] 모든 원소자 대문자 알파벳으로 구성된 문자열인지 검사 isupper()
data = "good"
print(f'{data} ==> {data.isupper()}')
print(f'GOOD ==> {"GOOD".isupper()}')
print(f'Good ==> {"Good".isupper()}')

## [3] 모든 원소자 소문자 알파벳으로 구성된 문자열인지 검사 islower()
print(f'GOOD ==> {"GOOD".islower()}')
print(f'Good ==> {"Good".islower()}')
print(f'good ==> {"good".islower()}')

## [4] 모든 원소자 숫자로 구성된 문자열인지 검사 isdecimal()
print(f'1234      => {"1234".isdecimal()}')
print(f'Happy1234 => {"Happy1234".isdecimal()}')

## [5] 숫자와 문자가 혼합된 문자열인지 검사 isalnum()
print(f'1234      => {"1234".isalnum()}')
print(f'Happy1234 => {"Happy1234".isalnum()}')
print(f'Happy     => {"Happy".isalnum()}')

## [6] 공백문자 여부 검사 isspace()
print(f'1234     => {"1234    ".isspace()}')
print(f'         => {"    ".isspace()}')