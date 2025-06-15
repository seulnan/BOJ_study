n = int(input())
b = int(input())

CON = 10**9 + 7
def power(c, d):
    if d == 0: # 지수가 0이면 항상 1임
        return 1
    half = power(c, d//2)
    if d %2==0:
        return (half*half)%CON
    else:
        return (c*half*half)%CON

print(power(n,b))
