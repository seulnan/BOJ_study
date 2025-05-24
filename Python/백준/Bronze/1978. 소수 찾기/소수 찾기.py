n = int(input())
nums = list(map(int, input().split()))
res= 0

for num in nums:
    error=0
    # 소수의 특징이 뭐지? 약수가 1이랑 자기자신만 있는. 
    if num > 1:
        for i in range(2, int(num**0.5)+1): # num의 0.5제곱만 따져도됨,근데 range는 int만 가능
            if num % i ==0:
                error+=1
        if error ==0:
            res+=1
print(res)            