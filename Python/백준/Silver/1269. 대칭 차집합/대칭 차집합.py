import sys
input = sys.stdin.readline

a, b = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

# 대칭 차집합: A에만 있거나 B에만 있는 원소들
res = A ^ B   # 또는 A.symmetric_difference(B)

print(len(res))