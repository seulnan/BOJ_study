'''
2606 실버
1번 컴퓨터가 바이러스 걸렸을때, 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력.
일단 재귀 이용한 dfs 사용.
'''
import sys
input=sys.stdin.readline

n=int(input()) #정점수
m=int(input()) #간선수


# 단순히 graph[v], 즉 연결되어있는 정점의 visited=true로 변경
def dfs(v):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

graph=[[] for _ in range(n+1)] #0부터 n까지 세팅& 0은 안쓰고 1~n만 씀

for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited=[False]*(n+1)

# 1번정점과 연결되어있는 다른 정점들을 visited=true처리함
dfs(1)

# 파이썬 특성상 true는 내부적으로 정수 1, false는 정수 0으로 취급됨
# true인것만 sum하고 거기에서 1번노드 1개 빼면 정답
print(sum(visited)-1)
