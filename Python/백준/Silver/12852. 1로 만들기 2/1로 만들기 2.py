import sys
input = sys.stdin.readline

n=int(input())
dp=[0]*(n+1)
trace = [0] * (n + 1) # 경로 추적용
# dp[i]에 계산횟수를 저장하는 방식 i가 수, dp[i]가 계산횟수
# 출력값은 dp[i], i를 모두 출력해야??

for i in range(2,n+1):
    dp[i] = dp[i-1]+1
    trace[i]=i-1 # 1을빼는 값을 넣어야함
    if i%3==0 and dp[i] > dp[i // 3] + 1: # 조건문을 좀더 구체화시키면됨
        dp[i] = dp[i // 3] + 1
        trace[i] = i // 3
    if i%2==0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        trace[i] = i // 2


print(dp[n])
path = []
curr = n # 10 입력받음
while curr != 0:
    path.append(curr) # 10넣고 다시 9넣고
    curr = trace[curr] # trace[10]=9을 curr에 넣고 trace[9]=3을 curr에 넣고
print(" ".join(map(str, path)))
