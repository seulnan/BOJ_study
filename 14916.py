n = int(input())

result = 0
while True:
    if n % 5 == 0:
        result += n//5
        print(result)
        break
    n -= 2
    result += 1
    
    if n < 0:
        print(-1)
        break        
