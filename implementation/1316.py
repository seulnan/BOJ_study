import sys
input = sys.stdin.readline

n = int(input())

# cnt에 n을 넣고 그룹단어가 아니면 하나씩 빼는 방식
cnt = n

# n만큼 입력받고 그냥 바로 count 계산하는게 훨씬 나음
for i in range(n):
    word = input().strip()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)        