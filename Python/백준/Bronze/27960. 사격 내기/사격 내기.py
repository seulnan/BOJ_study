import sys
input = sys.stdin.readline

# 각 과녁은 사람별로 최대 한번만 맞힐 수 있음
# 근데 55점이 어떻게 이진수의 숫자들의 합으로 이루어져있는지 구하려면 이진수로 바꾸면됨
a, b = map(int, input().split())


# 근데 a와 b가 둘다 맞히거나 못맞힌건 전부 안맞혔고 -> 0으로 해야됨
# a, b 둘중 한명만 맞힌 표적은 맞혔음 -> 1로 해야됨(다르면 1, 같으면 0인 xor)
print(int(bin(a^b)[2:],2))
