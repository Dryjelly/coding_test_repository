# 플로이드

import sys
input = sys.stdin.readline

MAX = 99999999999

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수

graph = [[MAX]*n for _ in range(n)]

def Floyd_Warshall():
    for k in range(n):
        for i in range(n):
            if i == k: continue
            for j in range(n):
                if j == k or j == i: continue
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a-1][b-1] = min(c, graph[a-1][b-1])

Floyd_Warshall()

for g in graph:
    for c in g:
        if c == MAX: sys.stdout.write('0 ')
        else : sys.stdout.write(str(c)+' ')
    sys.stdout.write('\n')