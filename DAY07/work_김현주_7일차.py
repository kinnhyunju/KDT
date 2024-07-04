# p.270~271
# [22.9] 연습문제
a = ['alpha', 'bravo','charlie','delta','echo','foxtrot', 'golf','hotel','india']
b = [i for i in a if len(i) == 5]
print(b)

# [22.10] 심사문제
a,b = map(int,input().split())
nums=[2**i for i in range(a,b+1)]
nums.pop(1)
nums.pop(-2)
print(nums)

# p.328~329
# [25.7] 연습문제
maria = {'korean': 94, 'english': 91, 'mathematics': 89,'science': 83}
average = sum(maria.values())/len(maria)
print(average)


# [25.8] 심사문제 ===> 아직 안 배운 것 같아서 보류