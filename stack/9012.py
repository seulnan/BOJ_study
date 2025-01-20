import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    data = input().strip()
    stack_count = 0 
    # vps여부를 for문안에서도, 밖에서도 통일성있게 추적하기 위한 변수도입
    is_vps = True
    
    for char in data:
        if char == "(":
            stack_count +=1
        else:
            stack_count -= 1
        #  ) 개수가 ( 개수보다 더 많은 경우 no출력해야    
        if stack_count < 0:   
            print("NO")
            is_vps = False # 이렇게 해야 for문 break해도 자국남길수있음
            break         
    
    # 위에 for문에서 중간에 false로 바뀌면서 break안된경우는 판단해줘야됨
    if is_vps:
        if stack_count == 0:
            print("YES")
        else:
            print("NO")    
