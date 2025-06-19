# 이름: 상태 를 딕셔너리로 저장
import sys
input = sys.stdin.readline

n = int(input())
att = {}

for i in range(n):
    name, status = input().split()
    if status == 'enter':
        att[name] = 1
    else:
        del att[name]

print(*sorted(att.keys(), reverse=True),sep='\n')
