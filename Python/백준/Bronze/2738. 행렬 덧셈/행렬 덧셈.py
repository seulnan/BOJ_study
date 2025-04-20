A, B = [], []

N, M = map(int, input().split())

# 첫번째 행렬 append하기 
for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

# 두번째 행렬 append하기
for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)
    
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()