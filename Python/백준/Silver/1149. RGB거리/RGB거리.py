n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
# [[26 40 83],[49 60 57],[13 89 99]] 이렇게 담겨져있음

for i in range(1, n): # 1부터 n-1까지만
    cost[i][0] += min(cost[i-1][1], cost[i-1][2])
    cost[i][1] += min(cost[i-1][0], cost[i-1][2])
    cost[i][2] += min(cost[i-1][0], cost[i-1][1])
# 집 i를 특정 색으로 칠했을 때의 최소 누적 비용을 구하고 저장
# 그걸 다음 집(i+1) 계산할 때 기반으로!

print(min(cost[-1]))
# i = 1일 때는 집1의 값들로 집2 비용을 갱신
# i = 2일 때는 집2의 값들로 집3 비용을 갱신
# 결국 집1 → 집2 → 집3까지의 누적 최솟값이 계산됨(cost[-1]에서!그것중 젤 최솟값을 고르면됨)
