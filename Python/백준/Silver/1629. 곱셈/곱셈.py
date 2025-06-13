a, b, c = map(int, input().split())

def power(n,m): # n의 m제곱을 재귀로 구하는
    if m==0: # _의 0승은 언제나 1
        return 1
    half = power(n, m//2)

    if m % 2 == 0:
        return (half*half)%c # 모듈러 연산 이용해서 미리미리 나머지계산해두기
    else:
        return (half*half*n)%c

print(power(a,b)%c) # a의 b승
