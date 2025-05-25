m,n = map(int, input().split())

for num in range(m, n+1):
    # num이 소수면 출력하고, 아니면 출력안하기
    if num ==1:
        continue
    for j in range(2, int(num**0.5)+1):
        if num % j ==0: # 약수가 존재하므로 소수가 아님
            break # 더이상 검사할 필요가 없으므로 for문 j에서 벗어남
    else: 
        print(num)