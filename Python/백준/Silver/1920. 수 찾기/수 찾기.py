n = int(input())
check_A_num = set(map(int, input().split()))

m = int(input())
is_here_list = list(map(int, input().split()))
    
for i in is_here_list:
    print(1) if i in check_A_num else print(0)

# 이분탐색으로도 해봐야해