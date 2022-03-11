# 특정한 최단 경로

import sys, heapq
input = sys.stdin.readline

MAX = int(1e9)

N, E = map(int, input().split()) # 정점, 간선

graph = [[] for _ in range(N)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))

v1, v2 = map(int, input().split()) # 반드시 지나야 하는 정점

""" 시작점에서 v1, v2 까지의 거리중 짧은 거리 + v1, v2 사이의 거리 + 끝점에서 v1, v2 까지의 거리중 짧은 거리 """

def dijkstra(start_node, end_node):
    cost = [MAX for _ in range(N)]

    q = [(0, start_node)]
    cost[start_node] = 0

    while q:
        dist, node = heapq.heappop(q)
        if dist > cost[node]: continue
        for next_node, next_dist in graph[node]:
            new_cost = next_dist + dist
            if new_cost < cost[next_node]:
                cost[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))
    
    # print(cost)
    return [cost[n] for n in end_node]

# print(dijkstra(0))
# print(dijkstra(v1-1))
# print(dijkstra(N-1))

s_v1, s_v2 = dijkstra(0, [v1-1, v2-1])
v1_v2, v1_e = dijkstra(v1-1, [v2-1, N-1])
v2_v1, v2_e = dijkstra(v2-1, [v1-1, N-1])

answer = min(s_v1 + v1_v2 + v2_e, s_v2 + v2_v1 + v1_e)
if answer > MAX : answer = -1
print(answer)