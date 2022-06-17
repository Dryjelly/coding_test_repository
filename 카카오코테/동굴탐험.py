def solution(n, path, order):
    answer = True

    graph = [[] for _ in range(n)]
    p_graph = [[] for _ in range(n)]

    for n1,n2 in path:
        graph[n1].append(n2)
        graph[n2].append(n1)

    def dfs(node, p):
        for next in graph[node]:
            if next == p: continue
            p_graph[next].append(node)
            dfs(next, node)
    dfs(0,0)

    room_list = {}
    for key, room in order:
        if room == 0: return False
        p_graph[room].append(key)
        room_list[room] = False

    def go_to_root(node, visited):
        if node == 0: return True
        visited[node] = True
        for next in p_graph[node]:
            if visited[next]: visited[node] = False; return False
            if next in room_list and room_list[next] == True: continue
            if not go_to_root(next, visited): visited[node] = False; return False
            if next in room_list: room_list[next] = True
        visited[node] = False
        return True

    visited = [False for _ in range(n)]
    for room in room_list:
        if not go_to_root(room, visited): return False

    # print(p_graph)
    # print(graph)

    return answer


print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],
[[8,5],[6,7],[4,1]]))
print(solution(9,	[[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]],
[[4,1],[5,2]]))
print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],
[[4,1],[8,7],[6,5]]))