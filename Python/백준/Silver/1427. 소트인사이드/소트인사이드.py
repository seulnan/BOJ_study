# list는 문자열이나 리스트처럼 iterable(반복가능한) 자료형에서만 사용가능!!
n = list(input())

# sorted는 정렬된 새 리스트 반환, sort는 리스트 자체를 정렬함(inplace형태, 원본변경안됨)
# join은 리스트 요소들을 하나의 문자열로 합치는 함수
print("".join(sorted(n, reverse=True)))