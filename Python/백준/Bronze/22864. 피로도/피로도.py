# 시간당 피로도, 처리한 일 
# 피로도 m 넘으면 번아웃
pirodo = 0 # 피로도
work = 0 # 처리한 일
cnt = 0 # 24시간만 돌려야됨

A,B,C,M = map(int,input().split())

while cnt < 24: # 최대 24번 반복
    if pirodo+A <= M: # pirodo+A가 M보다 작을때까진 계속 일할수있음 같아지거나 초과한 순간 일을 더시킬수없음
        work += B
        pirodo += A
    else: # 쉬어야됨
        pirodo -= C
        if pirodo < 0: # 음수가 되면 0으로 초기화시켜야됨
            pirodo = 0 
    cnt += 1

print(work)    