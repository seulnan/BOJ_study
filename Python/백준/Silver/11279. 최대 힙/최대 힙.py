import sys
import heapq
input = sys.stdin.readline

"""
heapq 모듈 함수들 (최소힙기준으로 되어있음)
1. heapq.heappush(heap,item) 이 함수는 아이템을 힙에 추가
2. heapq.heappop(heap) 가장 작은 아이템을 빼고 그 값을 반환
3. heapq.heappushpop(heap,item) 아이템을 힙에 추가하고 가장 작은 아이템 반환
4. heapq.heapify(x) 리스트 x를 즉시 heap으로 변환 - O(n)
"""

n = int(input())
max_heap = []

# 입력이 실시간으로 들어오고 빠져나가는 구조로
for _ in range(n):
    number = int(input())
    if number > 0:
        heapq.heappush(max_heap, -number) # 최소힙이 아니라 최대힙이라 음수로 변경해서 넣기

    else:
        if not max_heap: # 저장된 숫자가 없다면
            print(0)
        else:
            print(-heapq.heappop(max_heap)) # 부호 바꿨으니까 앞에 마이너스 붙여야
