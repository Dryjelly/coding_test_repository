# 미확인 도착지

import sys, heapq
input = sys.stdin.readline

MAX = 9999999

T = int(input()) # test case 개수

def dijkstra(start_node):
    cost = [MAX for _ in range(n+1)]
    cost[start_node] = 0
    q = [(0, start_node)]

    while q:
        dist, node = heapq.heappop(q)
        if dist > cost[node]: continue

        for next_node, next_dist in graph[node]:
            new_cost = dist + next_dist
            if new_cost < cost[next_node]:
                cost[next_node] = new_cost
                heapq.heappush(q,(new_cost, next_node))

    return cost

for _ in range(T):
    n,m,t = map(int, input().split()) # 교차로, 도로, 목적지 후보
    s,g,h = map(int, input().split()) # 출발지, g, h 사이를 지나갔음

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int, input().split()) # a, b 사이에 길이 d 인 도로
        graph[a].append((b,c))
        graph[b].append((a,c))

    goal = [int(input()) for _ in range(t)] # 목적지 후보

    cost = dijkstra(s)
    cost_g, cost_h = dijkstra(g), dijkstra(h)
    result = []
    for g_c in goal:
        result.append([g_c,cost[g]+cost_h[g_c]+cost_g[h]])
        result.append([g_c,cost[h]+cost_g[g_c]+cost_h[g]])

    answer = set([])
    for node, dist in result:
        if cost[node] < dist: continue
        answer.add(node)
    answer = list(answer)
    answer.sort()
    for i in answer:
        print(i)