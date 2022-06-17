import heapq

def solution(n, paths, gates, summits):
    answer = []
    global result

    gates, summits = set(gates), set(summits)

    graph = [[] for _ in range(n+1)]
    for i,j,w in paths:
        graph[i].append((j,w))
        graph[j].append((i,w))

    result = [50000, 10000000]

    def BFS(start):
        global result
        visited = [False for _ in range(n+1)]
        visited[start] = True
        q = [(0, start)]
        it = 0

        while(q):
            c_w, node = heapq.heappop(q)
            it = max(it, c_w)
            if node in summits:
                if it <= result[1]:
                    if it == result[1] and node > result[0]: return
                    result = [node, it]
                    print(f'도착 {result}')
                return
            print(f'현재 node {node} iter {it}')
            for next, w in graph[node]:
                if visited[next]: continue
                if w > result[1]: continue
                if next != start and next in gates: continue
                if next not in summits: visited[next] = True
                heapq.heappush(q,(w,next))

    # for g in gates: print(f'{g} 에서 시작! ');DFS(g)
    for g in gates: print(f'{g} 에서 시작! ');BFS(g)

    return result

print(solution(6,	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
[1,3],[5])) # 5,3
print("\n")
print(solution(7,		[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],
[3,7],[1,5])) # 5,1
print("\n")
print(solution(5,[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],
[1,2],[5]))#5,6