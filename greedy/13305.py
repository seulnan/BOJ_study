import sys
input = sys.stdin.readline

n = int(input())

length = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
a = price[0]

# 거리개수만큼 반복해야(length[i]) 그래서 n이 아니라 n-1임 
for i in range(n-1):
    if price[i] < a:
        a = price[i]
    result += a * length[i]    
    
print(result)    