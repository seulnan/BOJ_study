import sys
input = sys.stdin.readline

n,m = map(int, input().split())
name = set()
result = []

for i in range(n):
    name.add(input().strip())

for i in range(m):
    find = input().strip()
    if find in name: # 리스트기반말고 set로 하면 해시테이블구조라 O(1)임
        result.append(find)

result.sort()
print(len(result))
print(*result, sep="\n")
