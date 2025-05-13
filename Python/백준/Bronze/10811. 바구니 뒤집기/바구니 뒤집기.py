n,m=map(int,input().split())
# range(n)하면 바구니가 0부터 시작하기때문에 안됨
basket=[i for i in range(1, n+1)]

for i in range(m):
    j, k =map(int, input().split())
    # 주의!!바구니는 1번째부터 시작함!!!인덱스는 0부터 시작하니까 -1씩해야됨
    temp = basket[j-1:k]
    temp.reverse()
    basket[j-1:k]=temp # 업데이트하기
    
for i in range(n):
    print(basket[i], end=" ")
    