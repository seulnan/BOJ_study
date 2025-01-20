import sys
input = sys.stdin.readline

phrase = input().strip()

result = []
for char in phrase: 
    if char.isupper():
        result.append(char.lower())
    else:
        result.append(char.upper())

print("".join(result))