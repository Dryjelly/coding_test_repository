def solution(n, computers):
    answer = 0
    global visited
    visited = [False for _ in range(n)]

    def dfs(node):
        global visited
        for next_node in range(n):
            if computers[node][next_node] == 0 or visited[next_node] == True: continue
            else:
                visited[next_node] = True
                dfs(next_node)

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            dfs(i)
            answer += 1
        pass

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1