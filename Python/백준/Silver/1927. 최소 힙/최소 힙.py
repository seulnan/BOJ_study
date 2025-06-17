import sys
import heapq

input = sys.stdin.readline
n = int(input())
min_heap = []

for _ in range(n):
    num = int(input())
    if num >0:
        heapq.heappush(min_heap,num)
    else:
        if not min_heap:
            print(0)
        else:
            print(heapq.heappop(min_heap))