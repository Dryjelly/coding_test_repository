from collections import deque

def solution(n, edge):
    answer = 0

    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]

    for e in edge:
        graph[e[0]-1].append(e[1]-1)
        graph[e[1]-1].append(e[0]-1)
    # print(graph)

    q = deque(graph[0])
    visited[0] = True
    for i in graph[0]: visited[i] = True

    while(q):
        q_size = len(q)
        answer = q_size
        
        for i in range(q_size):
            next = q.popleft()
            for item in graph[next]:
                if visited[item]: continue
                visited[item] = True
                q.append(item)
        # print(q_size, q)

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)