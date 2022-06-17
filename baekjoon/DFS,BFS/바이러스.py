import sys
input = sys.stdin.readline

C = int(input())
E = int(input())

graph = [[] for _ in range(C+1)]
visited = [False for _ in range(C+1)]
cnt = 0

for e in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    global cnt
    if visited[node]: return
    visited[node] = True
    cnt += 1
    for next in graph[node]:
        dfs(next)

dfs(1)
print(cnt-1)
