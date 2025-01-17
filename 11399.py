n = int(input())

people_time = list(map(int, input().split()))

people_time.sort()
answer = 0 

for i in range(1, n+1):
    answer += sum(people_time[0:i]) # 리스트의 0번째 수부터 i번째수까지의 sum
    
print(answer)    
