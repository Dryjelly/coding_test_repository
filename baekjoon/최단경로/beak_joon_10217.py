# KCM Travel

import sys
from collections import deque
input = sys.stdin.readline

MAX = 999999999999

def dijkstra(graph, N, M):
    cost_dist = [[MAX]*(M+1) for _ in range(N)]
    cost_dist[0][0] = 0

    q = deque([(0,0,0)]) # dist, cost, node

    while q:
        c_dist,c_cost,c_node = q.popleft()
        if cost_dist[c_node][c_cost] < c_dist: continue

        for n_node, n_cost, n_dist in graph[c_node]:
            new_dist = c_dist + n_dist
            new_cost = c_cost + n_cost
            if new_cost > M: continue # 예산 초과
            if cost_dist[n_node][new_cost] <= new_dist: continue # 최소 거리 아님

            if cost_dist[n_node][0] > new_dist: cost_dist[n_node][0] = new_dist # 최소값 저장
            for i in range(new_cost, M+1):
                if cost_dist[n_node][i] > new_dist:
                    cost_dist[n_node][i] = new_dist
                else: break

            q.append((new_dist, new_cost, n_node))

    return cost_dist[-1][0]

T = int(input())

for t in range(T):
    N,M,K = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(K):
        u,v,c,d = map(int, input().split())
        graph[u-1].append((v-1,c,d))
        
    result = dijkstra(graph,N,M)
    if result == MAX: print('Poor KCM')
    else: print(result)

