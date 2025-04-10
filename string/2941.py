# c=, c-, dz=, d-, lj, nj, s=, z= 

crotia = ['c=', 'c-','dz=','d-','lj','nj','s=','z=']

word = input()

# 일반문자인지 저 크로티아 문자열인지 확실히 판별해야
# 파이썬의 특수한 함수인 replace를 활용하고 나머진 걍 len을 쓰면됨

for i in crotia:
    word = word.replace(i, "*")
print(len(word))    