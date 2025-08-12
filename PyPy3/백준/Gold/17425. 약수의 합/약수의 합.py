'''
풀이설계
단계적으로차근차근?
n이 주어졌을때 일단 for문으로 range(1, n+1)까지 돌려
그담에 f(y)를 실행하고 걍 그거 더하면되는거아냐?
근데 이제 굉장히 먼저 약수합을 전처리해야함
약수합을 어떤방법을 써도 O(n)이니까 금지임 걍 약수합을 구해야
'''

import sys
input=sys.stdin.readline

T = int(input())
qs = [int(input()) for _ in range(T)]
MAX = max(qs)

# 1. f[n] = n의 약수합 전처리
f = [0] * (MAX + 1)
for i in range(1, MAX + 1): # i: 약수후보
    for j in range(i, MAX + 1, i): # j: i의 배수들
        f[j] += i # i는 j의 약수이므로 더해줌

# 2. g[n] = f[1...MAX]를 누적합하면됨
g = [0] * (MAX + 1)
for i in range(1, MAX + 1):
    g[i] = g[i - 1] + f[i]

# 3. 한 줄에 하나씩 출력
print('\n'.join(str(g[n]) for n in qs))
