'''
문제설명
정육면체 상자가 일렬로 있음
앞에 있는 상자가 뒤보다 작으면 앞에 있는걸 뒤에있는거에 넣기
lis 걍 그대로인데??
'''

import sys
import bisect
input=sys.stdin.readline

n=int(input())
num=list(map(int, input().split()))

dp=[num[0]]

for i in range(n):
    if dp[-1] < num[i]:
        dp.append(num[i])
    else:
        idx=bisect.bisect_left(dp,num[i])
        dp[idx]=num[i]
print(len(dp))
