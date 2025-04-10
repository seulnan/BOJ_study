# 누적합이 100에 가까운 수여야 함
# 계속 더한걸 기존값과 꾸준히 비교해야함(끝까지?)??이러면 너무 비효율
# score - 100(100보다 클경우) & 100-score(100보다 작을 경우)를 계속 비교해야
# 어차피 끝까지 더해봐야하니까 score이 100보다 큰 경우였을때만 더 세세하게 따지면 됨


import sys
input = sys.stdin.readline

score = 0
mushroom = []

for _ in range(10):
    mushroom.append(int(input()))

for i in mushroom:
    score += i # i는 각각의 버섯점수를 순회함
    if score >= 100:
        
        if score - 100 > 100 - (score-i): # score-i가 score전의 점수를 의미!!!가 핵심포인트
            score -= i # i를 뺀 전단계가 더 작기때문에 간격이 더 작다가 포인트
            break
print(score)