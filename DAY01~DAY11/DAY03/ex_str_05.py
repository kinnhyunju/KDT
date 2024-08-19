# ------------------------------------------------------------------
# 문자열 str 데이터 다루기
# - 이스케이프 문자 : 특수한 의미를 가지는 문자
#   * 형식 : \문자1개
#   * '\n' - 줄바꿈 문자
#   * '\t' - 탭 간격 문자
#   * '\'' - 작은따옴표 문자
#   * '\"' - 큰따옴표 문자
#   * '\\' - 백슬래시 문자, 경로(path), URL관련
#   * '\U' - 유니코드
#   * '\a' - 알람소리 문자
# ------------------------------------------------------------------
msg = "오늘은 좋은날\n내일은 주말이라 행복해"
print(f"msg 줄바꿈 : {msg}")

msg = '오늘은 나의 "생일" 이야'
print(msg)

msg = '오늘은 나의 \'생일\' 이야'
print(msg)

file = 'C:\\Users\\kdp\\anaconda3\\test.txt'
print(file)

# r'   ' 또는 R'   ' : 문자열 내 이스케프 문자는 무시됨!
file =r'C:\Users\kdp\anaconda3\test.txt'
print(file)

msg = "Happy\tNew\tyear"
msg2 = R"Happy\tNew\tyear"
print(msg, msg2)