import sys
input=sys.stdin.readline

n,m= map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

result=[0]*(n+m)
i=0
j=0
k=0

while i<n or j<m:
    # j>m 을 먼저체크해야
    # 만약 i<n을 먼저체크하면 i=0, j=1일때
    # i<n and a[0]<b[1]이렇게 되면서 오류가 남
    # b[j]를 확인하기 전에 벗어나진않았는지 j>=m을 먼저 봐야함!!!!
    if j>=m or (i<n and a[i]<b[j]):
        result[k]=a[i]
        i+=1
    else:
        result[k]=b[j]
        j+=1
    k+=1

print(*result)
