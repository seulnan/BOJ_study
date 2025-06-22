import sys
input = sys.stdin.readline

n,m = map(int,input().split())
site ={}

for i in range(n):
    web, pw = map(str, input().split())
    site[web] = pw

for i in range(m):
    input_site = input().strip()
    print(site[input_site])
