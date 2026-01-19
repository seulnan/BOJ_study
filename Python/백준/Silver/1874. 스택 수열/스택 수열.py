'''
요구사항 분석
스택 -> 드럼통
LIFO

스택에 push하는 순서는 반드시 오름차순을 지킨다. 3 4 5 6 이런식으로
-> 핵심포인트: pop하는걸로 수열을 만들어야함!! (수열과 스택은 다른거임)

첫줄에 8
두번쨰줄부터 1~8 정수가 하나씩 순서대로 주어짐 (같은정수 두번 안나옴) -> 이게 수열
이 입력된 수열을 만들기 위해 필요한 연산을 한줄에 한개씩 출력

1 push 2 push 3 push 4 push

**4 pop [1,2,3]

**3 pop [1,2] top 2

4 push 5 push 6 push

**6 pop [1,2,3,4,5] top 5

7 push 8 push

**8 pop [1,2,5,7] top 7

**7 pop [1,2,5] top 5

**5 pop [1,2]

**2 pop

**1 pop

그때그때 +/- 출력하는게 중요할듯??
현재 top과 내가 뽑아야하는 숫자가 다르다면 그만큼 차근차근 push하고 pop해야됨

불가능은 대체 어떤케이스지? 반복문 쭉 돌았는데 안되면 그때 해야하는거같은데?

5
현재 top 0 투두 1
그래서 1 push
1 pop
2 push
2 pop

3 push 4 push 5 push 5 pop

근데 현재 top인 4가 목표치인 3보다 큼 -> 이때 불가능 판정이 나는구나!

최종 정리
현재 top과 내가 뽑아야하는 숫자가 다르다면 그만큼 차근차근 push하고 pop해야됨
근데 현재 top이 목표치보다 큼 -> 이때 불가능 판정이 나는구나!
'''

import sys
input=sys.stdin.readline

n=int(input())

numlist=[int(input()) for _ in range(n)]

cur=0 # 지금까지 push한 가장 큰 숫자

result=[] # + - 아니면 NO 넣을 리스트
stack=[] # 실제로 사용할 스택

for target in numlist: #numlist의 맨 앞부터 차근차근
    # top이 타겟보다 작다면 타겟이 될때까지 push하고 +출력
    # ***근데 if로하면 target당 한번만 push가능 -> while써야됨
    while cur<target:
        cur+=1
        stack.append(cur)
        result.append("+")

    # top이 타겟이랑 같다면 pop하고 -출력
    if stack and stack[-1]==target:
        stack.pop()
        result.append("-")

    # top이 타겟보다 크다면 바로 불가능 판정.
    else:
        print("NO")
        sys.exit()

print(*result,sep='\n')
