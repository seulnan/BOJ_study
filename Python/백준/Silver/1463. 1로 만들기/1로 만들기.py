import sys 
input = sys.stdin.readline

n = int(input())

dp = [0]*(n+1) # 인덱스 0부터 n까지 이용
# dp[1]=0, dp[2]=1, dp[3]=1, dp[4]=2
# dp[0]은 의미없음 리스트크기를 맞추기 위해 만들어둔것뿐
# dp[1] = 0 => 1을 1로 만드려면 최소계산횟수 0

for i in range(2,n+1):
    dp[i] = dp[i-1]+1 # 일단 이전값에 1빼는 계산했다고 가정하고 계산횟수 1더하기
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3]+1) #3으로 나눈 인덱스 에 3으로 나눈 계산횟수 1더하기
    if i%2==0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[n])        