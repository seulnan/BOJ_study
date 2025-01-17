n,k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

# k가 coins에 있는 값보다 크면 나누기 시작해야

answer = 0
for coin in coins:
    if k >= coin:
        answer += k // coin
        k %= coin # 나머지 할당 후 if문 반복
        if k <=0:
            break
print(answer)        