import sys
input = sys.stdin.readline
from collections import deque

# 초기 세팅
n = int(input())

d = deque()
    
for i in range(n):
    command = input().split()
    
    if command[0] == 'push_front':
        d.appendleft(command[1])
        
    elif command[0] == 'push_back':
        d.append(command[1])    
    
    elif command[0] == 'pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)       
            
    elif command[0] == 'pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)         
        
    elif command[0] == 'empty':
        print(0 if d else 1)            
    
    elif command[0] == 'size':
        print(len(d))
    
    elif command[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)             
    
    elif command[0] == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)           