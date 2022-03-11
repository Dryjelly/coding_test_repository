# 최단 경로
"""
import sys
input = sys.stdin.readline

MAX = 999999

V, E = map(int, input().split()) # 정점, 간선
graph = {i+1 : {} for i in range(V)}

s_p = int(input()) # 시작점

for _ in range(E):
    u, v, w = map(int, input().split()) # 시작, 도착, 가중치
    if v in graph[u]: # 다중 간선 체크 (최소 가중치만 남김)
        min_w = min(graph[u][v], w)
        graph[u][v] = min_w
    else:
        graph[u][v] = w

print(graph)

out = [False for _ in range(V)]
cost = [MAX for _ in range(V)] # max weight = 10
cost[s_p-1] = 0 # 시작점
node_num = V
node_cur = s_p

# Dijkstar
while(node_num):
    node_num -= 1
    for dst in graph[node_cur].keys(): # 현재 노드 탐색
        if out[dst-1]: continue
        if cost[dst-1] > graph[node_cur][dst] + cost[node_cur-1]: cost[dst-1] = graph[node_cur][dst] + cost[node_cur-1]
    out[node_cur-1] = True
    if node_num == 0: break

    min_value = MAX
    for node in range(1, V+1): # 다음 노드 선택
        if cost[node-1] < min_value and not out[node-1]:
            min_value = cost[node-1]
            node_cur = node

print(cost, out)
for c in cost:
    if c == MAX: print("INF")
    else: print(c)

"""
import sys, heapq
input = sys.stdin.readline
opt = sys.stdout.write

MAX = 999999
V, E = map(int, input().split()) # 정점, 간선

graph = {}
out = []
cost = []
for i in range(V):
    graph[i+1] = {}
    out.append(False)
    cost.append(MAX)

s_p = int(input()) # 시작점

for _ in range(E):
    u, v, w = map(int, input().split()) # 시작, 도착, 가중치
    if v in graph[u]: # 다중 간선 체크 (최소 가중치만 남김)
        min_w = min(graph[u][v], w)
        graph[u][v] = min_w
    else:
        graph[u][v] = w

print(graph)

cost[s_p-1] = 0 # 시작점
q = [(0 ,s_p)]

# Dijkstar
while q:
    weight, node_cur = heapq.heappop(q)
    out[node_cur-1] = True
    for dst in graph[node_cur].keys(): # 현재 노드 탐색
        if out[dst-1]: continue
        if cost[dst-1] > graph[node_cur][dst] + cost[node_cur-1]:
            cost[dst-1] = graph[node_cur][dst] + cost[node_cur-1]
            heapq.heappush(q, (cost[dst-1], dst))

print(cost, out)
for c in cost:
    if c == MAX: opt('INF\n')
    else: opt(f'{c}\n')