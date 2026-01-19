import sys
input=sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
stk = []
result = ['0'] * n #0으로 디폴트값 채우고 업데이트하는 방식 사용

for i in range(n-1, -1, -1): # 오른쪽부터 왼쪽으로 순회 O(n)
    # 하나의 i에 대해 조건이 만족할때까지 계속 비교 & 반복
    # but 어차피 pop 최대 n번, append 최대 n번이므로 O(n)유지
    while stk and num[i] >= stk[-1][1]: 
        result[stk.pop()[0]] = str(i+1)	# 수신하는 탑 번호 기록
    stk.append((i, num[i]))

print(*result)
