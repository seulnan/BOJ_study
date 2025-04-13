import sys
input = sys.stdin.readline  

N = int(input())
# 카운팅소트연습
count = [0] * 10001  # 0은 안 쓰고 1~10000까지만 씀, count[num+1]이런식으로 안하고 count[num]바로쓰도록.

for _ in range(N):
    num = int(input())
    count[num] += 1

for i in range(1, 10001):
    if count[i]:
        # i를 count[i]번 출력
        for _ in range(count[i]):
            print(i)