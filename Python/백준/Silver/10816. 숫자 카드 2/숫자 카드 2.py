import sys
input = sys.stdin.readline

from collections import Counter
# 데이터개수셀때 매우 유용한 파이썬

n = int(input())
cards = list(map(int, input().split()))

'''
Counter([6,3,2,10,10]) 이런식으로하면 내부적으로
{10:2,
3:1,
2:1, ...} 이런식으로 저장됨 10이라는게 2번저장되어있다
'''
cnt = Counter(cards) # 각 숫자의 등장횟수 저장 o(n)

m = int(input())
targets = list(map(int, input().split()))

result = [str(cnt[t]) for t in targets] # o(n)
# str로 바꿔야 Join가능
print(" ".join(result))
