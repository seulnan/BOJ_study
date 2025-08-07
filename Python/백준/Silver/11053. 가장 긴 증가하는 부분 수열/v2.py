'''
1. 수열을 순서대로 보면서, 현재 숫자를 기존 증가 수열 중 가장 적절한 자리에 넣자.
2. 끝에 넣을 수 있으면 넣자.
3. 아니면 기존 수열 중 자기보다 같거나 큰 숫자 중 가장 앞에 있는 것을 교체
'''
import sys
import bisect
input=sys.stdin.readline

n=int(input())

num=list(map(int, input().split()))
# 6개면 0~5까지
dp=[num[0]]

# 1부터 n-1까지 (1부터 5까지)
for i in range(1,n):
    if dp[-1] < num[i]:
        dp.append(num[i])
    else:
        idx=bisect.bisect_left(dp,num[i])
        dp[idx]=num[i]

print(len(dp))
