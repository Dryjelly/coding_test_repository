import heapq

def solution_2(n, costs): # dijkstra 로 풀었는데 아니였따~
    answer = 0
    visited = [False for _ in range(n)]
    cost = [None for _ in range(n)]
    cost[0] = 0

    graph = [[] for _ in range(len(costs))]
    for s,e,c in costs:
        graph[s].append((e,c))
        graph[e].append((s,c))

    visite_node = [(0,0,0)]
    while(visite_node):
        cur_cost, cur_node, prev_node = heapq.heappop(visite_node)
        if visited[cur_node]: continue
        visited[cur_node] = True
        answer += cur_cost - cost[prev_node]

        for next_node, next_cost in graph[cur_node]:
            if visited[next_node]: continue

            if cost[next_node] == None: # 처음 만나는 노드
                cost[next_node] = cur_cost + next_cost
            elif cur_cost + next_cost < cost[next_node]: # 현재 노드를 거쳐 가는게 더 이득
                cost[next_node] = cur_cost + next_cost
            else: continue
            
            heapq.heappush(visite_node,(cost[next_node],next_node, cur_node))


    print(cost)
    return answer

def solution_1(n, costs):
    answer = 0
    visited = [False for _ in range(n)]

    graph = [[] for _ in range(n)]
    for s,e,c in costs:
        graph[s].append((e,c))
        graph[e].append((s,c))

    visite_node = [(0,0)]
    while(visite_node):
        cur_cost, cur_node = heapq.heappop(visite_node)
        if visited[cur_node]: continue
        visited[cur_node] = True
        answer += cur_cost

        for next_node, next_cost in graph[cur_node]:
            if visited[next_node]: continue
            heapq.heappush(visite_node,(next_cost, next_node))
    
    return answer

def solution(n, costs):
    answer = 0

    costs.sort(key=lambda x: x[2])
    global root
    root = [i for i in range(n)]

    def union_fine(node):
        global root
        if root[node] == node: return node
        else:
            root[node] = union_fine(root[node])
            return root[node]

    bridges = 0
    for s,e,c in costs:
        if union_fine(s) == union_fine(e): continue
        answer += c
        root[union_fine(e)] = s
        bridges += 1
        if bridges == n-1: break

    print(root)
    
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])) # 4
print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]])) # 15
print(solution(6, [[0,1,2],[0,3,1],[0,4,5],[1,2,3],[1,3,2],[3,2,3],[3,4,1],[4,2,1],[4,5,2],[5,2,5]])) # 7
print(solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]])) #8
print(solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]])) #9
print(solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]])) #104
print(solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]])) #11
print(solution(5, [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]])) #6
print(solution(5, [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]])) #8
print(solution(5, [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]])) #8
