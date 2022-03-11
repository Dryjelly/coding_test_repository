# 타임머신

import sys
input = sys.stdin.readline

MAX = 99999999
N, M = map(int, input().split()) # 도시, 버스 노선 수

graph = [[] for _ in range(N+1)]

def Bellman_Ford():
    cost = [MAX for _ in range(N+1)]
    cost[1] = 0

    for _ in range(N-1):
        for cur_node in range(1, N+1):
            for next_node, next_cost in graph[cur_node]:
                if cost[cur_node] == MAX: continue
                new_cost = cost[cur_node] + next_cost
                if new_cost < cost[next_node]:
                    cost[next_node] = new_cost

    #print(cost)
    for cur_node in range(1, N+1):
        for next_node, next_cost in graph[cur_node]:
            new_cost = cost[cur_node] + next_cost
            if new_cost < cost[next_node] and cost[next_node] != MAX:
                return [0, 0, -1]

    return cost

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

#print(graph)
dist = Bellman_Ford()
for d in dist[2:]:
    if d == MAX: d = -1
    print(d)