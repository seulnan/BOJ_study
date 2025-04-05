import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))

dp = [0]*(n+1) # 인덱스 혼동 때문에 n+1로(인덱스 0은 0으로 사용x)

for k in range(1,n+1):
    dp[k] = dp[k-1]+arr[k-1] # 1번째부터 k번째까지의 합 미리 구하기

for _ in range(m):
    i,j = map(int,input().split())
    print(dp[j]-dp[i-1]) # j번째~i번째까지의 합을 빠르게 구할 수 있음