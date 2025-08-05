'''
알고리즘 설명
1. dp[i]를 다 1로 초기화
2. 0<=j<i && A[j] < A[i] 인 모든 j에 대해 max(dp[i], dp[j]+1) 를 dp[i]에 담음
'''
import sys
input = sys.stdin.readline

n=int(input())

dp=[1]*(n)
A=list(map(int, input().split()))

for i in range(n): # 현재 위치 i
    for j in range(0,i): # i보다 앞에 있는 모든 j에 대해
        if A[i] > A[j]: # 증가수열 조건 만족시
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))
