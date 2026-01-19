'''
LCS 알고리즘 설명
1. 두 수열 A, B 의 길이를 각각 n,m 이라 함
2. 크기가 (n+1)*(m+1)인 2차원 dp 배열을 0으로 초기화
++) n이 아니라 n+1하는 이유는 인덱스에러방지
dp[i][j] = A[0...i-1](길이가 i만큼) 와 B[0...j-1]의 LCS 길이
3. 현재 비교하는 원소 A[i-1]와 B[j-1]가 같으면 dp[i][j]=dp[i-1][j-1]+1
    공통문자열에 A[i-1]=B[j-1]값이 추가되기때문
4. 다르면 dp[i][j]=max(dp[i-1][j], dp[i][j-1])
    하나씩 빼보고 뭐가 더 큰지 담기
5. 모든 반복이 끝나면 dp[n][m]가 LCS의 최종길이
'''
import sys

def lcs(a, b):
    n=len(a)
    m=len(b)

    dp=[[0]*(m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1] == b[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]

# 입력전체를 한꺼번에 읽는 read사용, EOF까지 모든 내용을 문자열로 반환
text=sys.stdin.read().split()
for i in range(0,len(text),2):
    print(lcs(text[i], text[i+1]))
