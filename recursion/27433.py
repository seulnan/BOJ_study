num = int(input())

# 팩토리얼 출력
# 1부터 n까지 하나씩 곱하면됨
result = 1 # 0이면 뭘 곱해도 다 0이라 1로 초기값 설정
for i in range(2, num+1):
    result *= i
    
print(result)

# 재귀함수로도 풀어보기 
# 0보다 크거나 같은 정수 n의 n!을 구해야하므로 
# 0! & 1!은 1임 나머지는 기존사고대로 1*2*...*n-1*n이렇게 해야함
def factorial(n):
    if n <= 1:
        return 1 # result에 담지말고 그냥 값을 Return하면됨
    else:
        return n*factorial(n-1) # n! 은 n*(n-1)!임 (n-1)!은 (n-1)*(n-2)!임

print(factorial(num))