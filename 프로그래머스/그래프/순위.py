def solution(n, results):
    answer = 0

    graph_win = [set([]) for _ in range(n+1)]
    graph_lose = [set([]) for _ in range(n+1)]

    for r in results:
        graph_win[r[0]].add(r[1])
        graph_lose[r[1]].add(r[0])

    print(graph_win)
    print(graph_lose)

    def DFS(graph):
        visited = [False for _ in range(n+1)]

        def dfs(node):
            visited[node] = True
            visited_node = set([])
            for next in graph[node]:
                if visited[next]: visited_node.update(graph[next])
                else: visited_node.update(dfs(next))
            graph[node].update(visited_node)
            return graph[node]

        for i in range(1,n+1):
            if not visited[i]: dfs(i)

    DFS(graph_win)
    DFS(graph_lose)
 
    print(graph_win)
    print(graph_lose)
    # print()

    for i in range(1,n+1):
        if len(graph_win[i]) + len(graph_lose[i]) == n-1: answer += 1

    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)