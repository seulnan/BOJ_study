#nlogn을 이용할것
import sys
input = sys.stdin.readline  # 빠른 입력

n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()  # 또는 arr = sorted(arr)

for num in arr:
    print(num)