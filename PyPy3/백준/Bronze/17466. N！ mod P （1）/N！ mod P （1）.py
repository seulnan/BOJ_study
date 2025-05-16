import sys
input = sys.stdin.readline
n, p = map(int, input().strip().split())

if n >= p:
    print(0)
else:
    result = 1
    for i in range(2, n + 1):
        result = (result* i) % p
    print(result%p)