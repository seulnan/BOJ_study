# 이전의 결과가 후에 어떻게 영향을 미치는가??
# 3일 10, 1,20, 2,15 45
# 5일 20
# 1일 10, 1일 20, 2일 15,
# t를 누적시켜서 이게 7이 초과되면 안됨

import sys
input=sys.stdin.readline

N = int(input())
TP = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N-1,-1,-1):
    if i+TP[i][0]>N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max (dp[i+1],dp[i+TP[i][0]]+TP[i][1])
print(dp[0])
