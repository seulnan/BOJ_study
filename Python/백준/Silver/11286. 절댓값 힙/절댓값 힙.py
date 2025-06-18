import sys
import heapq
input = sys.stdin.readline

n = int(input())
min_heap = []

for _ in range(n):
    num = int(input())
    # 비교는 절댓값으로 하는데 만약 절댓값이 같다면 더 작은 음수를 출력해야해
    if num != 0:
        # 튜플을 이용해서 절댓값도 넣고 원래 숫자도 넣어
        # 정렬할때 쓰는 비교는 첫번째요소인 절댓값 그다음 원래값
        heapq.heappush(min_heap, (abs(num), num))
        # 그럼 [(1,-1),(1,1),(2,-2)] 이렇게 됨
    else:
        if not min_heap:
            print(0)
        else:
            print(heapq.heappop(min_heap)[1]) # 원래값 출력

# 들어온값이 양수일때랑 음수일때랑 나눠서 생각하면 될것같은데?
