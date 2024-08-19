while True:
    num = int(input('홀수차 배열의 크기를 입력하세요: '))
    if num%2 ==0: 
        print('짝수를 입력하였습니다. 다시 입력하세요.')
        continue

    else:
        rows = num
        columns = num
        mgsq = [[0 for col in range(columns)]for row in range(rows)]
        print(f'Magic Square ({num}x{num})')

        r=0
        c = columns//2
        mgsq[r][c] = 1
        for i in range(2,num*num+1):
            r -= 1
            c += 1
            if r<0 and c==num:
                r+=2
                c-=1
                mgsq[r][c]=i
            elif r <0:
                r=num+r
                mgsq[r][c] = i
            
            elif c==num:
                c=c-num
                mgsq[r][c] = i
            
            elif mgsq[r][c]!=0:
                r+=2
                c-=1
                mgsq[r][c] = i
            
            else : mgsq[r][c] = i

        for r in range(rows):
            for c in range(columns):
                print(f'{mgsq[r][c]:2}',end=' ')
            print()
    break