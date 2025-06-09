# list에 다 넣고 하나씩 for문에 인덱스 넣고 다 같으면 append result에 넣기?

n = int(input())
str_list = []
result = []
for _ in range(n):
    str_list.append(input())
# ["config.sys","config.inf","configures"] 이런식으로 나옴

size = len(str_list[0])

# 3개를 어떻게 한번에 비교하지?
# str_list[0][0] == str_list[1][0] == str_list[2][0] 이건데?
for i in range(size):
    first = str_list[0][i]
    for j in range(1, n):
        if str_list[j][i] == first:
            continue
        else:
            first = "?" # 같지않으면 다른거니까 ?로 채워야함
            break
    result.append(first)
print(''.join(result))
