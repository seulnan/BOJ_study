import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

# graph[v]: 정점 v와 연결된 인접노드목록
def dfs(graph,v,visited):
    visited[v]=True 
    for i in graph[v]: # 정점 v와 연결된 노드들 중에서
        if not visited[i]: # 노드 i에 대하여 visited가 False일때
            dfs(graph,i,visited) # 마찬가지로 dfs실행

n,m=map(int,input().split())            
# 인접리스트 사용
graph=[[] for _ in range(n+1)] #0부터 n까지하고 인덱스 0은 안씀

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v) 
    graph[v].append(u) # 양방향연결해야

count = 0 # 
visited = [False] * (n+1) # 0부터 n까지하고 인덱스 0은 안씀
for i in range(1, n+1): # 1번노드부터 n번노드까지 
    if not visited[i]: # dfs를 아직안한게 있나?
        dfs(graph, i, visited)
        count += 1 # dfs 한 번 끝날 때마다 count+1

print(count)