t = int(input())
    
# 어차피 개수니까 굳이 0.25로 안해도 됨 25로 하는게 입력값대할떄 더 편함     

for i in range(t):
    case = int(input())
    result = []
    for coin in [25,10,5,1]:
        # case에 있는 값이 코인단위보다 더 커야 진행할 필요가 없음
        # 어차피 0이면 0이 list에 들어가야됨
            result.append(case//coin)
            case = case % coin
    # 각 테스트케이스마다 담아서         
    print(*result)
