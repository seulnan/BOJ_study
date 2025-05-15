testcase = int(input())

for i in range(testcase):
    x1, y1, x2, y2 = map(int, input().split())
    planet_cnt = int(input())
    result = 0 # 이렇게 해야 매 테스트케이스마다 초기화됨
    for j in range(planet_cnt): # 행성끼리는 상관없음
        # 어차피 주요요인은 출발거리 < 반지름 & 종료점거리 > 반지름이라 내부에 있어서 이탈할 수 밖에없는
        # 출발점거리 > 반지름 & 종료점거리 < 반지름이라 외부에 있어서 진입할 수 밖에 없는
        cx, cy, cr = map(int,input().split())
        dist1=(x1-cx)**2+(y1-cy)**2 # 출발점과 행성중심간의 거리니까 제곱함
        dist2=(x2-cx)**2+(y2-cy)**2 # 종료점과 행성간의 거리
        if (dist1 < cr**2 and dist2 > cr**2) or (dist1 > cr**2 and dist2 < cr**2):
            result +=1
    print(result)
        