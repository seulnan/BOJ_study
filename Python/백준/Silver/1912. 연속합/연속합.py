'''
문제설명
n개의 정수로 이루어진 임의의 수열,
이 중 연속된 몇개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합
'''

'''
왜 dp를 사용해야하는가?
근데 여기에서 모든 구간의 부분합을 따지면 O(n^2)라 시간초과임
dp[i]=i번째 수까지 고려했을 때, i를 반드시 포함한 최대 연속 합으로 결정.
이전값을 이어받을지, 아니면 현재값부터 새로 시작할지 결정해야함
dp[i] = max(dp[i-1]+arr[i], arr[i])
'''

import sys
input = sys.stdin.readline

n=int(input())
# dp[i]=값담기 하려면 미리 크기를 지정해줘야함
# 파이썬 리스트는 dp.append(...)를 사용하지않고서는 빈 리스트에 바로 인덱스에 접근할 수 없다.
dp=[0]*(n)
arr=list(map(int, input().split()))

for i in range(n):
    dp[i]=max(dp[i-1]+arr[i], arr[i])

# 무작정 마지막원소를 포함한 연속합을 말해주는 건 아님
# 최대합은 중간지점 어딘가에서 끝날 수도 있잖아.
print(max(dp))
