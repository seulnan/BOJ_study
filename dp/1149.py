# RGB 거리엔 집이 n개

# 앞뒤로 같은색인지를 확인하고 같은 색이아닌것만 빼고?
n = int(input())
a = [0]*n

for i in range(n):
    a[i] = list(map(int,input().split()))
    
for i in range(1,n): # 1부터 시작하는 이유는 다음 입력값이 이전 입력값의 최소값을 사용하기때문이다
    a[i][0]= min(a[i-1][1],a[i-1][2]) + a[i][0]
    a[i][1]= min(a[i-1][0],a[i-1][2]) + a[i][1]
    a[i][2]= min(a[i-1][0],a[i-1][1]) + a[i][2]

print(min(a[n-1][0],a[n-1][1],a[n-1][2]))