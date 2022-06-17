import heapq

def solution(n, paths, gates, summits):
    answer = []
    global result

    gates, summits = set(gates), set(summits)

    graph = [[] for _ in range(n+1)]
    for i,j,w in paths:
        graph[i].append((j,w))
        graph[j].append((i,w))

    result = [9999999999, 9999999999]

    def dijkstra(start):
        global result
        distances = [9999999999] * (n+1)  # start로 부터의 거리 값을 저장하기 위함
        distances[start] = 0  # 시작 값은 0이어야 함
        queue = []
        heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

        while queue:  # queue에 남아 있는 노드가 없으면 끝
            current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.
            if distances[current_destination] < current_distance or result[1] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
                continue
            
            for new_destination, new_distance in graph[current_destination]:
                if new_destination in gates: continue
                distance = max(current_distance, new_distance)  # 해당 노드를 거쳐 갈 때 거리
                
                if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                    distances[new_destination] = distance
                    if new_destination in summits:
                        if distances[new_destination] <= result[1]:
                            if distances[new_destination] == result[1] and new_destination > result[0]: continue
                            result = [new_destination, distances[new_destination]]
                        continue
                    heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
        
        print(distances)
        for s in summits:
            if distances[s] <= result[1]:
                if distances[s] == result[1] and s > result[0]: continue
                result = [s, distances[s]]

    for g in gates: print(f'{g} 에서 시작! '); print(dijkstra(g))

    return result

print(solution(6,	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
[1,3],[5])) # 5,3
print("\n")
print(solution(7,		[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],
[3,7],[1,5])) # 5,1
print("\n")
print(solution(5,[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],
[1,2],[5]))#5,6