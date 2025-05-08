n = int(input())
arr = list(map(int, input().split()))

# 중복 제거 & 정렬     
unique =sorted(set(arr)) 
# -10 -9 2 4

# 각 값의 압축 좌표를 딕셔너리로 저장    
compressed={v:i for i,v in enumerate(unique)}
# {-10: 0, -9:1, 2:2, 4:3}

# 원래 배열arr의 요소를 인덱스로 삼은 딕셔너리에서 결과값 출력
# 문자열로 iterable 가능한 객체만 있으면 됨
# join 함수가 제너레이터객체받아서 자동으로 반복하면서 문자열 연결
print(' '.join(str(compressed[x]) for x in arr))