import sys
input=sys.stdin.readline
# 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에있는 수를 찾아야함

n = int(input())
num=list(map(int, input().split()))
stk=[0]
result=[-1]*n
# 예시 3 5 2 7 에서 NGE(2), NGE(3)이 둘다 7로 겹칠까?? 그 이유가 뭘까??
# 기대 5 7 7 -1
# 만약 5에서 오른쪽으로 순회하다가 5보다 큰 7을 만나면 기록해뒀는데,
# 순회과정중에 있는 숫자들은 5보다 작을 수 밖에 없음
# 그러면 그 중간에 있는 숫자들도 다 7이 됨

for i in range(1,n): # 1부터 n-1까지 순회
    # 하나의 i에 대해 만족할 때까지 반복
    while stk and num[i] > num[stk[-1]]:
        result[stk.pop()]=num[i]
    stk.append(i)

print(*result)

# i=1일때부터 오른쪽으로 순회
# num[1] 5 > num[0] 3 true
# result[0]=num[1] 5

# i=2일때
# num[2] 2 > num[1] 5 false
# stk=[0,1,2]

# i=3
# num[3] 7 > num[2] 2 true
# result[2]=7
# num[3] 7 > num[1] 5 true
# result[1]=7

# 비교숫자에 변화를 줘야함
# i로 변화를 주는게 아니라 stk 로 변화를 줘야함