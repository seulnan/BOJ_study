n = int(input())
# 초기값세팅
fib = [0 for _ in range(n+1)]
fib[1] =1

for i in range(2, n+1):
    fib[i] = fib[i-1] + fib[i-2]

print(fib[n])
