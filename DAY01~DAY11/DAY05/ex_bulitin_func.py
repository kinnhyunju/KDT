# -------------------------------------------------------------------------------------------
# 내장함수 
# -------------------------------------------------------------------------------------------
## 정수 관련 내장함수
## 2진수(컴), 8진수, 10진수(사람), 16진수(프로그램)

# 정수 ==> 2진수 변환해주는 내장함수   bin(정수) ==> 0b2진수    str타입
print(4,bin(4),type(bin(4)))
# 정수 ==> 8진수 변환해주는 내장함수   oct(정수) ==> 0o8진수    str타입
print(4,oct(4),type(oct(4)))
print(8,oct(8),type(oct(8)))
# 정수 ==> 16진수 변환해주는 내장함수  hex(정수) ==> 0x16진수   str타입
print(8,hex(8),type(hex(8)))
print(17,hex(17),type(hex(17)))

# 16진수 ==> 10진수 변환해주는 내장함수 int('str형식 수',base=0)
print(int('0o034',base=0))