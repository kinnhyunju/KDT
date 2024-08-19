import random

hb_sticks = [0,0,0,0]
nb_sticks = [0,0,0,0]


n_total_score = 0
h_total_score = 0

while True:
    while True:
        if h_total_score >= 20 : break
        for i in range(4):
            hb_sticks[i] = random.randint(0,1)

        h_score = hb_sticks.count(0)

        if h_score==0:
            h_score = 5

        h_total_score = h_total_score+h_score
        result = ['도','개','걸','윷','모']

        print(f'흥부 {hb_sticks}, {result[h_score-1]} ({h_score}점)/ (총 {h_total_score}점) --->')
    
        if h_score>3: continue
        else : break

    if h_total_score >= 20 : 
        print(f'흥부 승리 => 흥부: {h_total_score}, 놀부 : {n_total_score}')
        break

    
    while True:
            if n_total_score >=20 : break
            for i in range(4):
                nb_sticks[i] = random.randint(0,1)

            n_score = nb_sticks.count(0)

            if n_score==0:
                n_score = 5

            n_total_score = n_total_score+n_score
            result = ['도','개','걸','윷','모']

            print(f'                                    <--- 놀부 {nb_sticks}, {result[n_score-1]} ({n_score}점)/ (총 {n_total_score}점)')
            
            if n_score>3: continue
            else : break

    if n_total_score >=20 : 
        print(f'놀부 승리 => 놀부: {n_total_score}, 흥부 : {h_total_score}')
        break    


# 흥부만 이기게 만드는 함수
def winning():
    hb_sticks = [0,0,0,0]
    nb_sticks = [0,0,0,0]


    n_total_score = 0
    h_total_score = 0
    while True:
        while True:
            if h_total_score >= 20 : break
            for i in range(4):
                hb_sticks[i] = random.randint(1,1)

            h_score = hb_sticks.count(0)

            if h_score==0:
                h_score = 5

            h_total_score = h_total_score+h_score
            result = ['도','개','걸','윷','모']

            print(f'흥부 {hb_sticks}, {result[h_score-1]} ({h_score}점)/ (총 {h_total_score}점) --->')
        
            if h_score>3: continue
            else : break

        if h_total_score >= 20 : 
            print(f'흥부 승리 => 흥부: {h_total_score}, 놀부 : {n_total_score}')
            break
        while True:
            if n_total_score >=20 : break
            for i in range(4):
                nb_sticks[i] = random.randint(0,1)

            n_score = nb_sticks.count(0)

            if n_score==0:
                n_score = 5

            n_total_score = n_total_score+n_score
            result = ['도','개','걸','윷','모']

            print(f'                                    <--- 놀부 {nb_sticks}, {result[n_score-1]} ({n_score}점)/ (총 {n_total_score}점)')
            
            if n_score>3: continue
            else : break
            
        if n_total_score >=20 : 
            print(f'놀부 승리 => 놀부: {n_total_score}, 흥부 : {h_total_score}')
            break    


# # 아래 2줄의 주석을 삭제하면 실행 결과 3번이 실행 가능합니다.
# print('\n','-'*20,'최상/최악의 경우','-'*20,sep='')
# winning()