# 666 이 포함되어야함
# 근데 딱히 규칙이 없음-> 그럼 걍 일일이 하나하나 다 더하는수밖에

import sys
input=sys.stdin.readline

cnt=0 # n이 되면 멈추자.
n=int(input())
num=665

while cnt<n: #n과 같아지면 멈추기
    num+=1

    if '666' in str(num):
        cnt+=1

print(num)
