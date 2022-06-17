def solution(info, edges):
    global answer
    answer = 0
    graph = [[] for _ in range(len(info))]
    for s,e in edges: graph[s].append(e)
    print(graph)

    def dfs(cur_node, next_node, wolf, sheep):
        global answer
        if info[cur_node]: wolf += 1
        else: sheep += 1
        if wolf == sheep: answer = max(answer, sheep); return

        all_node = next_node[:] + graph[cur_node][:]
        if not all_node: answer = max(answer, sheep); return

        for idx, next in enumerate(all_node):
            dfs(next, all_node[:idx]+all_node[idx+1:], wolf, sheep)

    dfs(0,[],0,0)
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],
[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))

print(solution([0,1,0,1,1,0,1,0,0,1,0],
[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))