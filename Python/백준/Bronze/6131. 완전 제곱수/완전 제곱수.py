N = int(input())
cnt = 0

# a, b 선언해서 직접더하는것보다 range와 for이용해서 하는게 더좋음
for i in range(1,N):
    if i**2 > (i-1)**2+N:
        break
    for j in range(1, i+1):
        if i**2 == j**2+N:
            cnt +=1     
       
print(cnt)    