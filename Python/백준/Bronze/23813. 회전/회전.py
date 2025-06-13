n = list(input())
total = 0
for i in range(len(n)): # 다시 돌아오려면 딱 len(n)만큼 반복하면 됨
    n.insert(0, n[-1]) 
    del n[-1]
    total += int("".join(n))
print(total)