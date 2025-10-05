# queue를 이용하면될듯
import queue
q=queue.Queue()
# q=[]
import sys
input=sys.stdin.readline

n=int(input())

for i in range(n): #1부터 n까지
    q.put(i+1)
# 여기까지 시간복잡도 O(n)

for i in range(n-1):
    q.get()
    temp=q.get()
    q.put(temp)
# 이것도 get 2번+put1번 -> O(n-1)
# 근데 이걸 N-1번 반복 -> O(n)

print(q.queue[0])
