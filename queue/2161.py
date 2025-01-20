import sys
input = sys.stdin.readline

n = int(input())
card = []
result = []

for i in range(1, n+1):
    card.append(i)

# 제일 위에 있는 카드 버리기 & 추적
while len(card) != 0:
    result.append(card.pop(0))
    # 그래도 card가 안비었다면 위에 있는걸 아래로 보냄
    if len(card) != 0:
        card.append(card.pop(0))
    
# 출력 
print(*result)    