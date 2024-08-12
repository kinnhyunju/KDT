import re
# compile 사용 안함
m = re.match('[a-z]+', 'Python')
print(m)
print(re.search('apple', 'I like apple!'))
print(re.match('[a-z]+', 'pythoN'))

# compile 사용 : 객체 생성
p = re.compile('[a-z]+')
m = p.match('python')
print(m)
print(p.search('I like apple 123'))

# match() : 문자열의 처음부터 검사 -------------------------------------------------------------------
print('\nmatch() : 문자열의 처음부터 검사')
m = re.match('[a-z]+', 'pythoN')
print(m)

m = re.match('[a-z]+', 'PYthon')
print(m)

print(re.match('[a-z]+', 'regex python'))
print(re.match('[a-z]+', ' regexpython'))   # 문자열 처음에 공백 포함

print(re.match('[a-z]+', 'regexpythoN'))
print(re.match('[a-z]+$', 'regexpythoN'))   # $ : 문자여르이 마지막에 소문자 1회 이상 검사

print(re.match('[a-z]+', 'regexPython'))
print(re.match('[a-z]+$', 'regexpython'))

# findall() 함수 -----------------------------------------------------------------------------------
print('\nfindall() 함수')
p = re.compile('[a-z]+')
print(p.findall('life is too short! Regular expression test'))

# search() 힘수 ------------------------------------------------------------------------------------
print('\nsearch() 함수')
result = p.search('I like apple 123')
print(result)

result = p.findall('I like apple 123')
print(result)

import re
# ^ ... $ 을 명시해야 정확한 자리수 검사가 이루어짐
tel_checker = re.compile(r'^(\d{2,3})-(\d{3,4})-(\d{4})$')
print(tel_checker.match('02-123-4567'))

match_groups = tel_checker.match('02-123-4567').groups()
print(match_groups)
print('group 사용 :',tel_checker.match('02-123-4567').group())

print(tel_checker.match('053-950-45678'))
print(tel_checker.match('053950-4567'))

# dash(-) 제거하고 검사하기
print('\ndash제거하고 검사하기')
tel_number = '053-950-4567'
tel_number = tel_number.replace('-','')
print(tel_number)

tel_checker1 = re.compile(r'^(\d{2,3})(\d{3,4})(\d{4})$')
print(tel_checker1.match(tel_number))
print(tel_checker1.match('0239501234'))

# group() 사용
print('\ngroup() 사용')
m = tel_checker.match('02-123-4567')

print(m.groups())
print('group(): ',m.group())
print('group(0): ', m.group(0))
print('group(1): ',m.group(1))
print('group(2,3): ', m.group(2,3))
print('start(): ', m.start())           # 매칭된 문자열의 시작 인덱스
print('end: ',m.end())                  # 매칭된 문자열의 마지막 인덱스+1

cell_phone = re.compile('^(01(?:0|1|[6-9])-(\d{3,4})-(\d{4}))$')

print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567'))
print(cell_phone.match('010-1234567'))

import re

# 전방 탐색 (lookahead) -------------------------------------------------------------
# 전방 긍정 탐색 : (문자열이 패턴을 포함하고 있으면 패턴 앞의 문자열 리턴)
lookahead1 = re.search('.+(?=won)','1000 won')
if lookahead1 != None:
    print(lookahead1.group())
else:
    print('None')

lookahead2 = re.search('.+(?=am)','2023-01-26 am 10:00:01')
print(lookahead2.group())

# 전방 부정 탐색 (?!): 문자열 다음에 패턴을 포함하지 않으면 앞의 문자열 리턴
lookahead3 = re.search('\d{4}(?!-)','010-1234-5678')
print(lookahead3)

# 후방 탐색 (lookbehind) -------------------------------------------------------------
# 후방 긍정 탐색
lookbehind1 = re.search('(?<=am).+','2023-01-26 am 11:10:01')
print(lookbehind1)

lookbehind2 = re.search('(?<=:).+', 'USD: $51')
print(lookbehind2)

# 후방 부정 탐색
lookbehind3 = re.search(r'\b(?<!\$)\d+\b', 'I paid $30 for 100 apples.')
print(lookbehind3)