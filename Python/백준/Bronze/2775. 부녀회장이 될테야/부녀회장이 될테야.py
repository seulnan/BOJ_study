'''
문제설명
a층의 b호에 살려면 a-1층의 1호부터 b호까지의 사람들의 수 합만큼 살아야
k층의 n호에 몇명이 살고있냐??
0층의 i호에는 i명이 살고있음
'''

'''
이게 왜 dp지??
재귀적 관계 & 중복적인 하위계산이 발생함
a층의 b호를 알려면 a-2호의 1호는 b번, a-2호의 2호는 b-1번, a-3호의 3호는 b-2번, 이렇게 됨

f(k,n) = f(k-1,1)+f(k-1,2)+f(k-1,3)+,,,+f(k-1,n)
어떤값을 반복해서 더하는 구조 -> 테이블을 이용해 누적합을 저장하거나 반복문으로 계산하는 dp가 유리함
'''

'''
풀이설계
dp[a][b]: a층의 b호에 사는 사람이라하자.

점화식도출
**근데 a층의 b호는 a층의 b-1호(a-1층의 1~b-1호들의 합)에 a-1층의 b호를 더하면 됨**
dp[a][b] = dp[a][b-1]+dp[a-1][b]
'''

#a,b는 1보다 크고 14보다 작기떄문에 0부터 14까지 생성
dp=[[0]*(15) for _ in range(15)]

# 0층은 미리 준비해두자. 0층의 i호에는 i명이 살고있음
for i in range(1,15):
    dp[0][i] = i

# dp[a][b] 채우기
for a in range(1,15):
    for b in range(1,15):
        dp[a][b] = dp[a][b-1] + dp[a-1][b]

import sys
input=sys.stdin.readline

n = int(input())
for j in range(n):
    k=int(input())
    n=int(input())
    print(dp[k][n])
