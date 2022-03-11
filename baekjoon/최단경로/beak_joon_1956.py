import sys, heapq
input = sys.stdin.readline
MAX = 9999999999

V,E = map(int, input().split())
# graph = [[] for _ in range(V)]

# for _ in range(E):
#     a,b,c = map(int, input().split())
#     graph[a-1].append((b-1, c))

# def dijkstra(node):
#     cost = [MAX for _ in range(V)]
#     #cost[node] = 0
#     q = [(0, node)]
#     while q:
#         c_cost, c_node = heapq.heappop(q)
#         if c_cost > cost[c_node]: continue
#         for n_node, n_cost in graph[c_node]:
#             new_cost = c_cost + n_cost
#             if new_cost < cost[n_node]:
#                 cost[n_node] = new_cost
#                 heapq.heappush(q, (new_cost, n_node))
#     return cost

# cost = []
# for v in range(V):
#     cost.append(dijkstra(v))

# min_cost = MAX
# for i in range(V):
#     round_cost = cost[i][i]
#     if round_cost < min_cost: min_cost = round_cost

# print(f'cost = {cost}')
# print(min_cost if min_cost < MAX else -1) 

graph = [[MAX]*V for _ in range(V)]

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a-1][b-1] = c

def Floyd_Warshall():
    for k in range(V):
        for i in range(V):
            if i == k: continue
            for j in range(V):
                if j == k: continue
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

Floyd_Warshall()

min_cost = MAX
for v in range(V):
    graph[v][v]
    if graph[v][v] < min_cost: min_cost = graph[v][v]

print(min_cost if min_cost < MAX else -1) 