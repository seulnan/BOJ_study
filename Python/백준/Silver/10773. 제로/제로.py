import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    find = int(input())
    if find == 0:
        stack.pop()
    else:
        stack.append(find)

print(sum(stack))
