from collections import deque

def solution(places):
    answer = []

    def bfs(map, i, j):
        move = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = [[False]*5 for _ in range(5)]
        q = deque([])
        q.append((i,j))
        visited[i][j] = True
        dist = 0
        while(q and dist < 2):
            level = len(q)
            for _ in range(level):
                ci, cj = q.popleft()
                for m in move:
                    ni, nj = ci+m[0], cj+m[1]
                    if ni >= 5 or nj >= 5 or ni < 0 or nj < 0: continue
                    if visited[ni][nj] == True: continue
                    if map[ni][nj] == 'X': continue
                    if map[ni][nj] == 'P': return False
                    visited[ni][nj] = True
                    q.append((ni,nj))
            dist += 1
        return True

    def check(map):
        for i in range(5):
            for j in range(5):
                if map[i][j] == 'P':
                    if not bfs(map,i,j): return False
        return True

    for p in places:
        if check(p): answer.append(1)
        else: answer.append(0)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

# [1,0,1,1,1]