import sys
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

# 가장 작은 수인 2부터 시작해서 몇번나눠는지 세고 안나눠질때까지 나눠졌으면 다음숫자로 넘어가

def factorization(n): # 주어진 n을 소인수분해하는 함수
    i = 2  # 소인수 분해를 시작할 수
    while i * i <= n: # i가 n의 제곱근 이하일때까지 반복(그이후는 다 짝으로 나옴)
        count = 0  # i로 나눈 횟수(출력물의 뒷부분)
        while n % i == 0: # n이 i로 나눠떨어지는 동안 반복하여 count증가 & n을 i로 나눔
            count += 1 
            n //= i 
        if count > 0: 
            print(f"{i} {count}")
        i += 1 # 다음 소인수분해수로 넘어감
    if n > 1:
        print(f"{n} 1")  # 남은 수가 1보다 크면 소수이므로 출력

T = int(input())

for _ in range(T):
    N = int(input())
    factorization(N)