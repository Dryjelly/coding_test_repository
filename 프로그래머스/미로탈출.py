import heapq
def solution(n, start, end, roads, traps):
    trap_idx = {t:i for i,t in enumerate(traps)}
    graph = [[{},{}] for _ in range(n+1)]

    def check(t,s):
        if (1 << trap_idx[t]) & s: return True
        return False

    for P,Q,S in roads:
        if Q not in graph[P][0]:
            graph[P][0][Q] = S # 정방향
            graph[Q][1][P] = S # 역방향
            continue
        if graph[P][0][Q] > S:
            graph[P][0][Q] = S
        if graph[Q][1][P] > S:
            graph[Q][1][P] = S
    
    # print(graph)

    def get_next(cur_node, s):
        next = []
        cur_node_is_on = False
        if cur_node in trap_idx: cur_node_is_on = check(cur_node, s)

        for next_node, next_dist in graph[cur_node][0].items(): # 정방향 체크
            next_node_is_on = False
            if next_node in trap_idx: next_node_is_on = check(next_node, s)
            if cur_node_is_on == next_node_is_on: next.append((next_node, next_dist)) # 같으면 추가

        for next_node, next_dist in graph[cur_node][1].items(): # 역방향 체크
            next_node_is_on = False
            if next_node in trap_idx: next_node_is_on = check(next_node, s)
            if cur_node_is_on != next_node_is_on: next.append((next_node, next_dist)) # 다르면 추가

        return next

    def dijkstra(node):
        dist = [[float('inf')]*(2**len(traps)) for _ in range(n+1)]
        dist[node][0] = 0
        q = [(dist[node][0] ,node, 0)]
        while(q):
            cur_dist, cur_node, s = heapq.heappop(q)
            if cur_node == end: return cur_dist
            if cur_dist > dist[cur_node][s]: continue
            for n_node, n_dist in get_next(cur_node, s):
                sum_dist = cur_dist + n_dist
                next_s = s^(1<<trap_idx[n_node]) if n_node in trap_idx else s
                if sum_dist < dist[n_node][next_s]:
                    dist[n_node][next_s] = sum_dist
                    heapq.heappush(q,(dist[n_node][next_s], n_node, next_s))
        return -1

    # print(dijkstra(start))

    return dijkstra(start)

print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2])) # 5
print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2, 3])) # 4