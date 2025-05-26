#9랑 6은 하나로 취급하고 한 세트에 2개씩 있다고 가정
# 숫자 하나당 몇번나오는지를 파악하면 그게 즉 result임
# 근데 그게 9나 6이면 2로 나눠서 몫+1(홀) Or 몫(짝)이어야하고, Ex. 999에서 홀수면 몫+1
from math import ceil # 반올림함수

num = input()
checked = [0]*10 #0부터 9까지 총 10개

for ch in num:
    checked[int(ch)]+=1

six_nine=checked[6]+checked[9]
checked[6]=ceil(six_nine/2)
checked[9]=0 #checked[6]으로 통합했으니 0으로 무시하게 둠

print(max(checked))