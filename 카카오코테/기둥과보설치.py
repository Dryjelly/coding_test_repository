def solution(n, build_frame):
    answer = []

    # wall = [[[0,0]]*(n+1) for _ in range(n+1)]
    wall = [[[0,0] for _ in range(n+1)] for _ in range(n+1)]
    
    def check(x,y,a,b):
        if b: # 설치
            if a: # 보
                if wall[x][y-1][0]: return 1 # 밑 왼쪽에 기둥이 존재
                if wall[x+1][y-1][0]: return 1 # 밑 오른쪽에 기둥이 존재
                if x>0 and wall[x-1][y][1] and wall[x+1][y][1]: return 1 # 양쪽에 보가 존재
                return 0
            else: # 기둥
                if y == 0: return 1 # 바닥에 설치
                if wall[x][y-1][0]: return 1 # 밑에 기둥이 존재
                if wall[x][y][1]: return 1 # 밑 오른쪽에 보가 존재
                if x>0 and wall[x-1][y][1]: return 1 # 밑 왼쪽에 보가 존재
                return 0

        else: # 삭제
            assert wall[x][y][a]
            wall[x][y][a] = 0 # 일단 삭제 후 확인
            if a: # 보
                # 위 왼쪽에 기둥이 존재, 빼면 안됨
                if y<n and wall[x][y][0] and not check(x,y,0,1): wall[x][y][a] = 1; return 0 
                # 위 오른쪽에 기둥이 존재, 빼면 안됨
                if y<n and wall[x+1][y][0] and not check(x+1,y,0,1): wall[x][y][a] = 1; return 0 
                # 왼쪽에 보가 존재, 빼면 안됨
                if x>0 and wall[x-1][y][1] and not check(x-1,y,1,1): wall[x][y][a] = 1; return 0 
                # 오른쪽에 보가 존재, 빼면 안됨
                if wall[x+1][y][1] and not check(x+1,y,1,1): wall[x][y][a] = 1; return 0
                wall[x][y][a] = 1
                return 1
            else: # 기둥
                # 위에 기둥이 존재, 빼면 안됨
                if wall[x][y+1][0] and not check(x,y+1,0,1): wall[x][y][a] = 1; return 0 
                # 위 왼쪽에 보가 존재, 빼면 안됨
                if x>0 and wall[x-1][y+1][1] and not check(x-1,y+1,1,1): wall[x][y][a] = 1; return 0 
                # 위 오른쪽에 보가 존재, 빼면 안됨
                if wall[x][y+1][1] and not check(x,y+1,1,1): wall[x][y][a] = 1; return 0
                wall[x][y][a] = 1
                return 1

    for x,y,a,b in build_frame:
        if b: # 설치
            if check(x,y,a,b): wall[x][y][a] = 1
        else: # 삭제
            if check(x,y,a,b): wall[x][y][a] = 0
    
    # print(wall)

    for i in range(n+1):
        for j in range(n+1):
            if wall[i][j][0]: answer.append([i,j,0])
            if wall[i][j][1]: answer.append([i,j,1])

    return answer

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
result = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

print(result, '\n', solution(n,build_frame))

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
result = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

print(result, '\n', solution(n,build_frame))