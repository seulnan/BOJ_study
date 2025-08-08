'''
문제설명
KOI 어린이집에는 n명의 아이들
위치를 옮기는 아이들의 수를 최소로. 움직이는.
'''

'''
풀이구상
근데 이건 걍 정렬하고 cnt세면되는거아닌가?
아근데 정렬방법에 따라 달라져서??

3 7 5 2 6 1 4

왜 4번아이를 7뒤로 옮기지?
3 5 6 이 lis고, 아 lis요소 빼고 해야하는구나.
어떻게 보면 4&7 트레이드, 1&2 트레이드네.
아니그럼 걍 전체-lis길이아냐??
'''

import sys
import bisect
input=sys.stdin.readline

n=int(input())
num=[]

for i in range(n):
    num.append(int(input()))

dp=[num[0]]

for i in range(1,n):
    if dp[-1] < num[i]:
        dp.append(num[i])
    else:
        idx=bisect.bisect_left(dp, num[i])
        dp[idx]=num[i]
print(n-len(dp))
