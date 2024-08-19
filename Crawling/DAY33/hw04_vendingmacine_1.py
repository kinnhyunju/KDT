# 도저히 클래스로 구현을 못하겠습니다.....ㅠㅠ
# 더 공부해서 다음에는 꼭 완성하겠습니다......


# class VendingMachine:
#     def __init__(self, input_dict):
#         self.input_money = 0
#         self.inventory = input_dict

#     def run(self):
#         coin = int(input('동전을 투입하세요: '))
#         if coin < 300:
#             print(f'투입된 돈 ({coin}원)이 300원 보다 작습니다.')
#             print(f'{coin}원을 반환합니다.')
#             end()


# 메뉴 출력
def menu(coin):
        print('-'*40)
        print(f'  커피 자판기 (잔액:{coin}원)')
        print('-'*40)        
        print(' 1. 블랙 커피')
        print(' 2. 프림 커피')
        print(' 3. 설탕 프림 커피')
        print(' 4. 재료 현황')
        print(' 5. 종료')
        num  = int(input('메뉴를 선택하세요: '))
        return num, coin

inventory_dict = {'coffee':100, 'cream':100, 'sugar':100, 
                  'water':500, 'cup':5, 'change':0}

# 재료 현황
def prepare(coffee,cream,sugar,water, cup, change):
    print('-'*80)
    print('재료현황: ',end='')
    inventory_dict['coffee']-=coffee
    inventory_dict['cream']-=cream
    inventory_dict['sugar']-=sugar
    inventory_dict['water']-=100*water
    inventory_dict['cup']-=cup
    inventory_dict['change']+=300*change
    for k, v in inventory_dict.items():
        print(f'{k}: {v}',end='  ')
    print()
    print('-'*80)

# 재료 부족
def no_ingred():
      print('재료가 부족합니다.')
      prepare(0,0,0,0,0,0)

# 블랙 커피 만들기
def coffee_b(coin):
        print(f'블랙 커피를 선택하셨습니다. 잔액: {coin-300}')
        coin-=300
        # 커피 30g + 물 100ml
        prepare(30,0,0,1,1,1)
        return coin

# 프림 커피 만들기
def coffee_p(coin):
        print(f'프림 커피를 선택하셨습니다. 잔액: {coin-300}')
        coin-=300
        # 커피 15g + 프림 15g + 물 100ml
        prepare(15,15,0,1,1,1)
        return coin

# 설탕 프림 커피 만들기
def coffee_s(coin):
        print(f'설탕 프림 커피를 선택하셨습니다. 잔액: {coin-300}')
        coin-=300
        # 커피 10g + 프림 10g + 설탕 10g + 물 100ml
        prepare(10,10,10,1,1,1)
        return coin

    
# 끝내기
def end():
        print('-'*32)
        print('커피 자판기 동작을 종료합니다.')
        print('-'*32)

inventory_dict = {'coffee':100, 'cream':100, 'sugar':100, 
                  'water':500, 'cup':5, 'change':0}

def vending_machine():
      coin = int(input('동전을 투입하세요: '))
      while True:
            if coin<300:
                  print(f'투입된 돈 ({coin}원)이 300원보다 작습니다.')
                  print(f'{coin}원을 반환합니다.')
                  end()
                  break
            else:
                  num,coin = menu(coin)

                  if num == 1:
                        coin = coffee_b(coin)
                  elif num == 2:
                        coin = coffee_p(coin)
                  elif num == 3:
                        coin = coffee_s(coin)
                  elif num == 4:
                        prepare(0,0,0,0,0,0)
                  elif num==5 :
                        print(f'종료를 선택했습니다. {coin}원이 반환됩니다.')
                        end()
                        break
                  else : print('1~5 사이의 숫자만 입력하세요.')

                  if coin < 300:
                        print(f'잔액({coin}원)이 300원보다 작습니다.\n{coin}원을 반환합니다.')
                        end()
                        break
                  
                  if inventory_dict['coffee'] <10 or inventory_dict['cream']<10 or inventory_dict['sugar']<10 or inventory_dict['water'] <100 or inventory_dict['cup']<1:
                        no_ingred()
                        print(f'{coin}원을 반환합니다.')
                        end()
                        break

vending_machine()