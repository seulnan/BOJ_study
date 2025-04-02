# n번째 = n-1번째+n-2번째인데 
# n-1번째수는 n-2번째+n-3번째 
# 재귀는 어디부터 일반적이고 초반이 특수케이스니까 초반을 잘 구분해야

# n = 0 0 
# n = 1 1
num = int(input())

def fibo(n):
    if n <=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(num))    