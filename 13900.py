# n개의 정수 중 서로 다른 위치의 두 수를 뽑는 모든 경우의 두 수의 곱의 합

#list로 만들고
# list요소한개부터 이중 for문써서 
# for 요소 첫번째부터 그뒤요소 쭉 곱한걸 sum에 넣어
# 했더니 시간초과네?
# 더 효율적으로 생각해보려면 2,3,4,5 이렇게 있으면 
# 2*3 + 2*4 + 2*5 = 2*(3+4+5)
# 3*4 + 3*5 = 3*(4+5) 니까 

N = int(input())
num = list(map(int, input().split()))

total_sum = sum(num) # 요소들을 다 더하고 앞에서부터 하나씩 빼낸다 느낌
result = 0

for i in range(N):
    total_sum -= num[i]
    result += num[i] * total_sum

print(result)    