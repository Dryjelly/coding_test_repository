import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for m in range(M):
    n_1, n_2 = map(int, input().split())
    graph[n_1].append(n_2)
    graph[n_2].append(n_1)

for n in range(1,N+1): graph[n].sort()

# print(graph)

def DFS(start):
    result = []
    visited = [False for _ in range(N+1)]
    visited[start] = True

    def dfs(node):
        # print(node, end=' ')
        result.append(node)
        for next in graph[node]:
            if visited[next]: continue
            visited[next] = True
            dfs(next)

    dfs(start)
    print(' '.join(map(str,result)))

DFS(V)

def BFS(start):
    result = []
    visited = [False for _ in range(N+1)]
    visited[start] = True
    q = deque([start])

    while(q):
        node = q.popleft()
        # print(node, end=' ')
        result.append(node)
        for next in graph[node]:
            if visited[next]: continue
            visited[next] = True
            q.append(next)
    print(' '.join(map(str,result)))

BFS(V)