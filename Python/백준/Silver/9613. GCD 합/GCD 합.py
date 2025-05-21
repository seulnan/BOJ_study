# 가능한 모든쌍??이 뭔말이지?? 
# 근데 실제로 두개를 뽑아서 계속 계산하면 너무...오래걸리지않을까?
from itertools import combinations
from math import gcd

n = int(input())

for i in range(n):
    nums = list(map(int, input().split()))
    res = 0
    coms = combinations(nums[1:],2)
    for a, b in coms:
        res += gcd(a,b)
        
    print(res)