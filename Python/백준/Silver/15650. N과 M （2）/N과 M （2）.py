# 조합 어떻게 파이썬으로 구현
from itertools import combinations

n, m = map(int, input().split())
numList= [i for i in range(1,n+1)] # 1부터 N까지 담기

for seq in combinations(numList,m):
    print(*seq) # *은 unpacking임