num = input()
# 문자열은 iterable하다는걸 기억해두자. 인덱싱가능
# print(int(num[-1])+int(num[-2:]))
# 이렇게 하면 근데 b도 10일때 오류남
# 어차피 0<a,b<=10이니까 10일때를 따로 처리하자
if num[1]=="0": #0은 숫자가 아니라 string이다.
    print(10+int(num[2:]))
else:
    print(int(num[0])+int(num[1:]))