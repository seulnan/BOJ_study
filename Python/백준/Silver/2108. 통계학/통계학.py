'''
요구사항 분석
n은 홀수(감사합니다)
1. 산술평균: n개의 수들의 합(sum)을 n으로 나눈값 (avg)
2. 중앙값: n개의 수들을 오름차순으로나열 & 인덱스 상 중간으로 위치하는값
3. 최빈값: n개의 수들 중 가장 많이 나타남 -> 흠?ㅇ건 어케함?
4. 범위: n개의 수들 중 최댓값과 최솟값 차이(쏘이지 max min 차이 구하면되잖아)

어려운점
1. 반올림?? 을 어케 해 나 파이썬 함수몰라
2. 최빈값에서 여러개있으면 최빈값중 두번째로 작은 값 출력
3. 가장 많이 나타나는거..?를 어떻게 표현하지??기존에 리스트 쭉 돌고 in이 true면 그걸??하라고?흠
'''

import sys
input=sys.stdin.readline
from collections import Counter

n=int(input())
numlist=[int(input()) for _ in range(n)]

first=round(sum(numlist)/n) # 평균을 round를 이용해 반올림해야
print(first)

sorted_numlist=sorted(numlist,reverse=False) #오름차순
second=sorted_numlist[n//2]
print(second)

# 아 아니 최빈값어케 해?
counts=Counter(numlist)
max_freq = max(counts.values())
modes = [num for num, cnt in counts.items() if cnt == max_freq]
modes.sort()
# 같은값없으면, 즉 최빈값이 하나일때는 그냥 맨앞꺼 출력
if len(modes)==1:
    third=modes[0]
else:
    # 두개이상이라면, 오름차순으로 정렬한것중 맨앞에서 두번쨰.
    # 즉, 두번쨰로 작은것
    third=modes[1]

print(third)

four=sorted_numlist[-1]-sorted_numlist[0]
print(four)
