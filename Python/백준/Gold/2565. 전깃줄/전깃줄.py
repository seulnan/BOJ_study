'''
문제설명
아예 하나도 서로 교차하지않게 없애야하는 전깃줄의 최소개수.
-> 최대한 많이 남겨둬라
-> 가장 긴 길이의 수열을 만들어야함 그의 여집합을 구해야.
-> 근데 교차하지않아야하니까 a에 들어갈 숫자끼리도 생각해야하고, b에 들어갈 숫자끼리도 생각해야하고.

'''
import sys
import bisect

input=sys.stdin.readline

n=int(input())
num=[]

for i in range(n):
    num.append(list(map(int,input().split())))

# a기준으로 오름차순정렬을 미리 해두면, b만 가지고 lis문제를 만들 수 있기때문.
# a&b세트로 묶고 동시에 이동하도록설정하기만 하면됨.
num.sort(key=lambda x:x[0])
dp=[]
# 근데 일단 a랑 b 둘다 만족해야하니까.
# 8,9 했는데 안되니까 2,9로 대체
# 1,9로 대체하면서 4,3으로 되는데 그러면 겹치잖아 어차피 둘다 만족해야돼.

for a,b in num:
    #b값을 어쨌든 lis에 넣기 위한 위치를 찾는다. b가 들어갈 인덱스를 반환하도록.
    # 즉, dp[idx-1]<b<=dp[idx]를 만족하는 최소 idx
    # 2,3,5 이렇게 있으면 4를 정렬시킬거면 idx 2임
    idx=bisect.bisect_left(dp,b)
    # 2,3,5 이렇게 있는데 6을 정렬시킬거면 idx 3임 == len(dp) 맨끝이니까.
    if idx==len(dp):
        dp.append(b)
    else:
        # b를 삽입
        dp[idx]=b
# 여집합이니까 전체전깃줄 수 - LIS길이=제거할 최소 전깃줄 개수
print(n-len(dp))
