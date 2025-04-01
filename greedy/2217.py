# 물체의 최대 중량을 구해내는 프로그램 작성
# 모든 로프 사용할 필요 없음

# 총 중량 / 로프개수 = 로프 1개당 중량
# 총 중량 = 로프개수 * 로프1개당 중량 

n = int(input())

# 최소 중량을 드는 로프 * 개수하면안됨 (최소중량을 빼면됨)
ropes = []
for _ in range(n):
    ropes.append(int(input()))
    
ropes.sort()

result = []
for x in ropes:
    result.append(n*x)
    n -= 1
    
print(max(result))