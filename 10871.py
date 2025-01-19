n,x = map(int,input().split())

numbers = list(map(int, input().split()))
    
# 리스트 컴프리헨션 사용        
result = [i for i in numbers if i < x]        
        
print(*result)        