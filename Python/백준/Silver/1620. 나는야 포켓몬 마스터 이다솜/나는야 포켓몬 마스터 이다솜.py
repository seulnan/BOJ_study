import sys
input = sys.stdin.readline

n, m = map(int, input().split())
by_num = {}
by_name = {}

for i in range(1,n+1):
    poket = input().strip() # 줄바꿈문자가 있으니까
    by_num[poket] = i
    by_name[i] = poket
    # input() 을 두번 호출하면 두개의 Input이 들어가버림

for j in range(m):
    find = input().strip()
    if find.isdigit(): # 숫자로 찾아서 문자 출력해야
        # isdigit은 문자열이 숫자모양인지 판단할 뿐, 그 자료형은 여전히 str임
        print(by_name[int(find)])
    else: # 문자면 숫자 출력해야됨
        print(by_num[find])
