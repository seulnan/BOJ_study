from math import gcd
from itertools import combinations
n = int(input())

for i in range(n):
    nums = list(map(int, input().split()))
    res = 0 
    combs = combinations(nums[1:], 2) #nums의 인덱스 1인요소부터 2개씩 조합
    for a, b in combs:
        res += gcd(a,b)
    print(res)