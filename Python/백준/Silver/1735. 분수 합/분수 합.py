# 일단 최소공배수로 분모를 만들어야할듯
# 그담에 ( 최소공배수 // 분모 )를 분자에도 곱해서 두 분자를 더하기
# 그리고 분모가 최소공배수인 상태니까 기약분수라는건 두 수를 약분해야하는데
# 약분??을 어떻게 구현하지?? 두수의 최대공약수로 나눠야지 그럼 한번에 끝남

from math import gcd

def get_lcm(x, y):
    return x * y // gcd(x, y)

a_up, a_down = map(int, input().split())
b_up, b_down = map(int, input().split())

ab_lcm = get_lcm(a_down, b_down)

c_up = a_up * (ab_lcm // a_down) + b_up * (ab_lcm // b_down)
c_gcd = gcd(c_up, ab_lcm)

result_up = c_up // c_gcd
result_down = ab_lcm // c_gcd
print(result_up, result_down)