# 고민되는점: 뎁스가 계속 깊어지는데 이게 맞나?? if문안에 너무 뎁스가 깊어질것같음 how해결?
# 아 그냥 elif로 하면될수도..?
# 국어점수가 감소하는대로 = 국점수를 내림차순으로
# 영어점수가 증가하는대로 = 영점수를 오름차순으로
# ***추가적으로 시간복잡도를 생각하는법 : 1초에 대략 1억(10의 8승)번 연산가능
# 근데, 현재 n은 100,000임 & 시간제한 1초. 그니까 O(N^2)로 계산하면 10의 12승이라 시간초과

import sys
input = sys.stdin.readline

n = int(input())
student = []

# 코드를 최대한 간단하게 하기위해서 name이런식으로 대신 걍 student[0]사용하기(가독성을 위해서라면 필요하지만 ps라 생략)
for _ in range(n):
    student.append(input().split())

# key=로 간단하게 구현
student.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬한 정보에서 이름만 출력
for s in student:
    print(s[0])