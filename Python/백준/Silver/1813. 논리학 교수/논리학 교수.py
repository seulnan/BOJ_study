# 3이라면 3개있어야하고, 1이라면 1개있어야하고? -> count 활용하면될듯? 근데 문자열에서니까
# 매핑 필요

n = int(input())
result = 0
max = 0
n_list= list(map(int, input().split()))

for i in range(n):
    if n_list[i] == n_list.count(n_list[i]):
        max = n_list[i]
    if n_list[i] == 0 and n_list!=n_list.count(n_list[i]):
        max = -1
    if max>result:
        result=max

if max>=0:
    print(result)
else:
    print(max)                
