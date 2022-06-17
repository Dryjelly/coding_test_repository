from collections import defaultdict 

import sys
limit_number = 100000
sys.setrecursionlimit(limit_number)

def solution_2(arrows):
    global answer
    answer = 0
    graph = defaultdict(set)
    move = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]] # 0~7 / 오른쪽, 위로 갈때는 +1 그외 -1
    # 대각선 유의 1, 3, 5, 7

    cur = (0,0)
    for a in arrows: # 단방향 그래프 만들려고 했음...
        for _ in range(2): # 2번 이동 (대각선 처리위함)
            next = (cur[0]+move[a][0], cur[1]+move[a][1])
            if next in graph and cur in graph[next]: pass # 다음 노드가 이미 지나온 노드이고 현재 노드로 이어져 있으면 pass
            else: graph[cur].add(next) # 없으면 연결
            cur = next
    
    visited = set()

    # def check_diagonal(prev,x_m,y_m):
    #     p1 = (x_m+prev[0],prev[1])
    #     p2 = (prev[0],y_m+prev[1])
    #     if p2 in graph and p1 in graph[p2] and p2 in visited: return True
    #     if p1 in graph and p2 in graph[p1] and p1 in visited: return True
    #     return False

    def dfs(node, prev):
        global answer
        # 현재 움직임이 대각인 경우 겹쳐지면 answer += 1 해야함
        # x_m, y_m = node[0]-prev[0], node[1]-prev[1]
        # if x_m != 0 and y_m != 0:
        #     if check_diagonal(prev,x_m,y_m):
        #         answer += 1
        
        if node in visited: # 이미 방문한 노드
            answer += 1
            return

        visited.add(node)
        if node not in graph: return # 다음에 갈 곳 없으면 끝
        for next in graph[node]:
            dfs(next, node)


    # print(graph)
    dfs((0,0),(0,0))
    # print(visited)
    

    return answer

def solution(arrows):
    answer = 0
    move = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]] # 0~7 / 오른쪽, 위로 갈때는 +1 그외 -1
    line = set()
    point = set([(0,0)])

    cur = (0,0)
    for a in arrows: # 단방향 그래프 만들려고 했음...
        for _ in range(2): # 2번 이동 (대각선 처리위함)
            next = (cur[0]+move[a][0], cur[1]+move[a][1])
            if (cur,next) not in line: # 지나온 길 아님
                if next in point: # 방문했던 노드 만남
                    answer += 1

            point.add(next)
            line.add((cur,next))
            line.add((next,cur))
                    
            cur = next
    
    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]), 3)
print(solution([6, 0, 3, 0, 5, 2, 6, 0, 3, 0, 5]),3)

print(solution([6, 5, 2, 7, 1, 4, 2, 4, 6]),3)
print(solution([5, 2, 7, 1, 6, 3]),3)
print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]),3)

print(solution([2,5,2,7]))

print(solution([1]))

print(solution([6,6,0,3,0,3,4,7,4,7,4,1,4,1,0,5,0,2,6,5]),13)
