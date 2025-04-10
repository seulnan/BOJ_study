#연산을 하는 횟수의 최솟값을 출력하기

import sys
input = sys.stdin.readline

n = int(input())
count = 0

while n > 1:
    if n % 3 == 0:
        n = n/3
        count += 1
    elif n % 2 == 0:
        n = n/2
        count += 1
    else:
        n -= 1
        count += 1
    
print(count)