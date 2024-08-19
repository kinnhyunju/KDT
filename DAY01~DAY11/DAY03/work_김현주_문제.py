# 001
print("Hello World")
# 002
print("Mary's cosmetics")
# 003
print('신씨가 소리질렀다. "도둑이야".')
# 004
print('C:\Windows')
# 005
print("안녕하세요.\n만나서\t\t반갑습니다.") #\t : 탭, \n : 줄 바꿈 문자
# 006
print ("오늘은", "일요일") # ==> 오늘은 일요일 (데이터 사이에 한 칸 공백)
# 007
print('naver;kakao;sk;samsung')   # print('naver','kakao','sk','samsung',sep=';')
# 008
print('naver','kakao','sk','samsung',sep='/')
# 009
print("first",end='');print("second")
# 010
print(5/3)
# 011
삼성전자 = 50000
총평가금액 = 삼성전자*10
print(총평가금액)
# 012
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
# 013
s = "hello"
t = "python"
print(f'{s}! {t}')   # print(s+"!", t)
# 014
2 + 2 * 3       # 답 : 8
# 015
a = "132"
print(type(a)) # :str
# 016
num_str = "720"
print(int(num_str))
# 017
num = 100
print(str(num))
# 018
num_s = "15.79"
num_f = float(num_s)
print(num_f)
# 019
year = "2020"
year = int(year)
print(year, year-1, year-2)
# 020
    # 에어컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 
    # 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
fee = 48584
sum = fee * 36
print(sum)
# 021
letters = 'python'
print(letters[0],letters[2])
# 022
license_plate = "24가 2210"
print(license_plate[-4:])
# 023
string = "홀짝홀짝홀짝"
print(string[::2])
# 024
string = "PYTHON"
print(string[::-1])
# 025

# 026

# 027
url = "http://sharebook.kr"
print(url[-2:])
# 028
    # lang = 'python'
    # lang[0] = 'P'
    # print(lang)
    # 문자열에서는 자료 변경이 불가능하므로 오류 발생
# 029

# 030

# 031
a = "3"
b = "4"
print(a + b)    # "34"
# 032
print("Hi" * 3) # HiHiHi
# 033
print('-'*80)
# 034
t1 = 'python'
t2 = 'java'
msg = t1+' '+t2+' '
print(msg*4)
# 035
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이 : %d" %(name1,age1))
print("이름: %s 나이 : %d" %(name2,age2))
# 036

# 037
print(f'이름: {name1} 나이 : {age1}')
print(f'이름: {name2} 나이 : {age2}')

# 038

# 039
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
# 040
data = "   삼성전자    "
print(data.split())

# 051
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# 052

# 053

# 054
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[-2]
# 055
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[-2:]
print(movie_rank)
# 056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1+lang2
print(langs)
# 057
nums = [1, 2, 3, 4, 5, 6, 7]
print(f'max:  {max(nums)}')
print(f'min:  {min(nums)}')
# 058
nums = [1,2,3,4,5]
del sum
print(sum(nums))
'''질문
146번 줄에 있는 함수를 실행할때 아래와 같은 오류가 나왔습니다.
in <module>  
    print(sum(nums))
TypeError: 'int' object is not callable
검색을 해보니 예약어를 사용해서 발생하는 오류라 del을 실행하면 해결된다고 나왔는데
왜 오류가 발생했는지, 해결되는 원리가 뭔지 설명 알 수 있을까요?'''
# 059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))
# 060
nums = [1, 2, 3, 4, 5]
average = sum(nums) / 5 # len(nums)로 나눌 수 계산
print(average)
# 061
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
# 062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
# 063
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])
# 064
nums = [1, 2, 3, 4, 5]
print(nums[::-1])
# 065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])
# 066

# 067

# 068

# 069

# 070
data = [2, 4, 3, 1, 5, 10, 9]
# data1 = data.sort
# print(data1)
data.sort()
print(data)
# 071
my_variable=()
# 072
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
# 073
num = (1,)
# 074
'''>> t = (1, 2, 3)
>> t[0] = 'a'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t[0] = 'a'
TypeError: 'tuple' object does not support item assignment
'''
# 튜플은 자료 변경, 수정이 불가능한데 t의 0번 인덱스 값을 수정하려고 해서 오류가 발생함
    # tuple은 원소(element)의 값을 변경할 수 없습니다.
# 075
t = 1, 2, 3, 4      # 데이터 타입 : 튜플
# 076
t = ('a', 'b', 'c')
t = list(t)
t[0] = 'A'
t = tuple(t)
    # t = ('A', 'b', 'c')
print(t)
# 077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest)
# 078
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(interest)
# 079
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)    # => ['apple', 'banana', 'cake']
# 답 : apple banana cake
# 080
num = range(2,100,2)
nums = tuple(num)
print(nums)