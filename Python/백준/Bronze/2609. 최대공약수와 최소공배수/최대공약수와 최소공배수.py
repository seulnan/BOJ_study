a, b = map(int, input().split())

# a, b의 공약수는 a,b 모두를 나눌 수 있는 구조임.
# a = b*q+r, r = a - b*q이라 a, b공약수는 a, b 모두 나눌수있으니까 r을 나눌수있음
# a, b 의 공약수는 b, r의 공약수와 같음

# a,b의 대소관계는 어차피 위치 바뀌면서 나머지를 줄여가는 구조라서 자연스럽게 계산되어 예외처리 필요없음(나머지계산은 대소관계제약없음)
def gcd(a, b):
    while b > 0: #b가 0보다 클때까지 나머지연산, b가 0이되면 while탈출하고 a출력
        a, b = b, a%b
    return a

# a*b = 최소공배수 * 최대공약수
def lcm(a,b):
    return a*b // gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))