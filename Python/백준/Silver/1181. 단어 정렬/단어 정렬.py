n = int(input())
    
phrase = set()
for _ in range(n):
    phrase.add(input()) # set은 add로 요소추가

phrase=list(phrase) # list로 다시 변환
# sort는 문자까지 정렬해줌!!!
phrase.sort() # 괄호안에 아무것도 안넣으면 알파벳순서대로 정렬해줌
phrase.sort(key=len) # 그상태에서 문자열길이순으로 정렬하기

for i in phrase:
    print(i)