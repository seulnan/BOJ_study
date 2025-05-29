a = int(input()) # 원래 고기온도
b = int(input()) # 목표온도 
c = int(input()) # 얼어있는 고기를 데우는데 걸리는 시간 c
d = int(input()) # 얼어있는 고기를 해동하는데 걸리는 시간 d
e = int(input()) # 얼어있지않은 고기를 데우는데 걸리는 시간 e

time = 0 

while a < b: # a가 항상 b보다 작게 주어지므로 이렇게 세워도 됨
    if a < 0:
        time += c
        a += 1
    elif a == 0:
        time += d
        time += e # a==1만들어놔야 무한루프안됨
        a += 1  # 해동 후 바로 다음 온도로 넘어가야 반복됨
    else:
        time += e
        a += 1

print(time)
        