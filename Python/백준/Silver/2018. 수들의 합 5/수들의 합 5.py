import sys
input=sys.stdin.readline

n=int(input())
total=0
cnt=0
start,end=0,0

# end가 n이 아니기만 하면
while end!=n:
    # 합이 n보다 작으면 end를 하나 늘리고 total에 이를 추가
    if total<n:
        end+=1
        total+=end
    # 합이 n보다 크면 앞에 start을 빼고 start을 하나 늘리기
    elif total>n:
        total-=start
        start+=1
    else: # 합이 n과 같으면
        cnt+=1
        end+=1
        total+=end

print(cnt+1) # 자기자신도 포함해야함
