## [1] outer = 5, inner = 5
for i in range(5):
    for j in range(5):
        print(f'j:{j}',end=' ')
    print(f'i:{i}\\n')

# 계단식으로 별 출력
for i in range(5):
    for j in range(i+1):
        if i==j:
            print('*'*(i+1))

# 대각선으로 별 출력
for v in range(5):
    for h in range(v+1):
        # if h==v:
        #     print('*')
        # else:
        #     print(' ',end='')
        # 한줄로 바꾸면
        print('*' if h==v else ' ', end= '\n' if h==v else '')