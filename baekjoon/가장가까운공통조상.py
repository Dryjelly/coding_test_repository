import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    graph = [i for i in range(N+1)]
    for n in range(N-1):
        p, c = map(int, input().split())
        graph[c] = p
    # 찾기
    a, b = map(int, input().split())
    visited = set([a])
    
    while(graph[a] != a):
        a = graph[a]
        visited.add(a)
    while(b not in visited):
        b = graph[b]
    print(b)

# T = int(input())
# for t in range(T):
#     N = int(input())
#     graph = [0 for _ in range(N+1)]
#     level = [0 for _ in range(N+1)]
#     for n in range(N-1):
#         p, c = map(int, input().split())
#         graph[c] = p
#     # 찾기
#     a, b = map(int, input().split())
#     a_set, b_set = set([a]), set([b])
    
#     while True:
#         if graph[a]: a_set.add(graph[a])
#         if graph[b]: b_set.add(graph[b])

#         if graph[a] and graph[a] in b_set: print(graph[a]); break 
#         if graph[b] and graph[b] in a_set: print(graph[b]); break 

#         if graph[a]: a = graph[a]
#         if graph[b]: b = graph[b]
