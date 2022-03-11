from collections import deque
import copy

# def solution(board):
#     answer = 0
#     robot_pos = [[0,0],[0,1]]
#     N = len(board)
#     # init (wall -> -1)
#     for r in range(N):
#         for c in range(N):
#             if board[r][c]: board[r][c] = -1
#     board_path = [copy.deepcopy(board), copy.deepcopy(board)]

#     def check(locs):
#         for loc in locs:
#             # 보드 범위 검사
#             if loc[0]<0 or loc[0]>=N: return False
#             if loc[1]<0 or loc[1]>=N: return False
#             # 벽 검사
#             if board[loc[0]][loc[1]] == -1: return False
#         return True

#     def rotate_check(start_loc, end_loc):
#         # 회전 범위 검사
#         s_r = min(start_loc[0], end_loc[0])
#         s_c = min(start_loc[1], end_loc[1])
#         if board[s_r][s_c] == -1: return False
#         if board[s_r][s_c+1] == -1: return False
#         if board[s_r+1][s_c] == -1: return False
#         if board[s_r+1][s_c+1] == -1: return False
#         return True

#     def rotate(pos):
#         new_pos = []
#         cw_rotation_matrix = [[0, -1], [1, 0]]
#         ccw_rotation_matrix = [[0, 1], [-1, 0]]
#         # 1번 축 기준 회전 (x, y)
#         loc = [pos[1][1] - pos[0][1], pos[1][0] - pos[0][0]]
#         # 시계 방향
#         new_loc = [cw_rotation_matrix[1][0] * loc[0] + cw_rotation_matrix[1][1] * loc[1],
#                    cw_rotation_matrix[0][0] * loc[0] + cw_rotation_matrix[0][1] * loc[1]]
#         new_loc[0], new_loc[1] = new_loc[0]+pos[0][0], new_loc[1]+pos[0][1]
#         mid_loc = [[new_loc[0], pos[1][1]],[new_loc]]
#         if check([new_loc]) and rotate_check(pos[1], new_loc):new_pos.append([pos[0], new_loc])
#         # 반시계 방향
#         new_loc = [ccw_rotation_matrix[1][0] * loc[0] + ccw_rotation_matrix[1][1] * loc[1],
#                    ccw_rotation_matrix[0][0] * loc[0] + ccw_rotation_matrix[0][1] * loc[1]]
#         new_loc[0], new_loc[1] = new_loc[0]+pos[0][0], new_loc[1]+pos[0][1]
#         if check([new_loc]) and rotate_check(pos[1], new_loc): new_pos.append([pos[0], new_loc])

#         # 2번 축 기준 회전 (x, y)
#         loc = [pos[0][1] - pos[1][1], pos[0][0] - pos[1][0]]
#         # 시계 방향
#         new_loc = [cw_rotation_matrix[1][0] * loc[0] + cw_rotation_matrix[1][1] * loc[1],
#                    cw_rotation_matrix[0][0] * loc[0] + cw_rotation_matrix[0][1] * loc[1]]
#         new_loc[0], new_loc[1] = new_loc[0]+pos[1][0], new_loc[1]+pos[1][1]
#         if check([new_loc]) and rotate_check(pos[0], new_loc): new_pos.append([new_loc, pos[1]])
#         # 반시계 방향
#         new_loc = [ccw_rotation_matrix[1][0] * loc[0] + ccw_rotation_matrix[1][1] * loc[1],
#                    ccw_rotation_matrix[0][0] * loc[0] + ccw_rotation_matrix[0][1] * loc[1]]
#         new_loc[0], new_loc[1] = new_loc[0]+pos[1][0], new_loc[1]+pos[1][1]
#         if check([new_loc]) and rotate_check(pos[0], new_loc): new_pos.append([new_loc, pos[1]])

#         return new_pos

#     def move(pos):
#         new_pos = []
#         # 상
#         if check([[pos[0][0]-1, pos[0][1]], [pos[1][0]-1, pos[1][1]]]):
#             new_pos.append([[pos[0][0]-1, pos[0][1]], [pos[1][0]-1, pos[1][1]]])
#         # 하
#         if check([[pos[0][0]+1, pos[0][1]], [pos[1][0]+1, pos[1][1]]]):
#             new_pos.append([[pos[0][0]+1, pos[0][1]], [pos[1][0]+1, pos[1][1]]])
#         # 좌
#         if check([[pos[0][0], pos[0][1]-1], [pos[1][0], pos[1][1]-1]]):
#             new_pos.append([[pos[0][0], pos[0][1]-1], [pos[1][0], pos[1][1]-1]])
#         # 우
#         if check([[pos[0][0], pos[0][1]+1], [pos[1][0], pos[1][1]+1]]):
#             new_pos.append([[pos[0][0], pos[0][1]+1], [pos[1][0], pos[1][1]+1]])

#         return new_pos

#     def is_valid(pos, step):
#         # 드론이 가로
#         if pos[0][0] == pos[1][0]: select_board = board_path[0]
#         # 드론이 세로
#         elif pos[0][1] == pos[1][1]: select_board = board_path[1]
#         # 현 위치가 최소거리인가?
#         flag = False
#         for loc in pos:
#             r,c = loc
#             if select_board[r][c] == 0: select_board[r][c] = step; flag = True # 새로운 노드 도착
#             elif select_board[r][c] >= step: select_board[r][c] = step; flag = True # 최소거리로 노드 도착
#         return flag

#     def is_end(pos):
#         for loc in pos:
#             if loc == [N-1, N-1]: return True
#         return False

#     # print(board)
#     # print(rotate(robot_pos))
#     # print(move(robot_pos))
#     # print(rotate(robot_pos)+move(robot_pos))

#     q = deque([robot_pos])
#     step = 1

#     while q:
#         count = len(q)
#         for c in range(count):
#             pos = q.pop()
#             if not is_valid(pos, step): continue
#             if is_end(pos): print(board_path[0]); print(board_path[1]); return step-1
#             next_pos = rotate(pos) + move(pos)
#             for n_p in next_pos:
#                 q.appendleft(n_p)
#         step += 1
#     print(board)
#     return -1

def solution(board):
    direction = [[-1,0],[0,1],[1,0],[0,-1]] # 상, 우, 하, 좌 (시계방향)
    robot_pos = [0,0,1] # 0,0 위치 + 오른쪽 방향으로 한칸
    N = len(board)

    def is_valid(loc):
        # 입력받은 위치가 board의 범위를 벗어나는지, 벽인지 판단하는 함수
        # 보드 범위 검사
        if loc[0]<0 or loc[0]>=N: return False
        if loc[1]<0 or loc[1]>=N: return False
        # 벽 검사
        if board[loc[0]][loc[1]] == 1: return False
        return True

    def pivot_change(pos):
        # 기준점 변경
        d = pos[-1]
        new_d = (pos[-1]+2)%4
        new_pos = [pos[0]+direction[d][0], pos[1]+direction[d][1], new_d]
        return new_pos

    def rotate(pos):
        new_pos = []
        # 1번축 기준으로 회전
        cw_d = (pos[-1]+1)%4 # 시계방향
        ccw_d = (pos[-1]-1)%4 # 반시계방향
        if is_valid([pos[i] + direction[pos[-1]][i] + direction[cw_d][i] for i in range(2)]) and is_valid([pos[i] + direction[cw_d][i] for i in range(2)]): new_pos.append(pos[:-1] + [cw_d])
        if is_valid([pos[i] + direction[pos[-1]][i] + direction[ccw_d][i] for i in range(2)]) and is_valid([pos[i] + direction[ccw_d][i] for i in range(2)]): new_pos.append(pos[:-1] + [ccw_d])
        # 2번축 기준으로 회전
        pos = pivot_change(pos)
        cw_d = (pos[-1]+1)%4 # 시계방향
        ccw_d = (pos[-1]-1)%4 # 반시계방향
        if is_valid([pos[i] + direction[pos[-1]][i] + direction[cw_d][i] for i in range(2)]) and is_valid([pos[i] + direction[cw_d][i] for i in range(2)]): new_pos.append(pos[:-1] + [cw_d])
        if is_valid([pos[i] + direction[pos[-1]][i] + direction[ccw_d][i] for i in range(2)]) and is_valid([pos[i] + direction[ccw_d][i] for i in range(2)]): new_pos.append(pos[:-1] + [ccw_d])
        return new_pos

    def move(pos):
        new_pos = []
        for d in range(4):
            m_loc_1 = [pos[i] + direction[d][i] for i in range(2)] # 기준점
            m_loc_2 = [m_loc_1[i] + direction[pos[-1]][i] for i in range(2)] # 나머지
            if is_valid(m_loc_1) and is_valid(m_loc_2): new_pos.append(m_loc_1 + [pos[-1]])
        return new_pos

    def is_end(pos):
        if pos[:-1] == [N-1, N-1]: return True
        if [pos[i] + direction[pos[-1]][i] for i in range(2)] == [N-1, N-1]: return True
        return False

    q = deque([robot_pos])
    visited = set([tuple(robot_pos), tuple(pivot_change(robot_pos))])
    step = 0

    while q:
        count = len(q)
        for c in range(count):
            pos = q.pop()
            if is_end(pos): print(board); return step
            next_pos = rotate(pos) + move(pos)
            for n_p in next_pos:
                if tuple(n_p) not in visited:
                    q.appendleft(n_p)
                    visited.add(tuple(n_p))
                    visited.add(tuple(pivot_change(n_p)))
        step += 1
    return -1

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
result = 7
print(solution(board), result)

board = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]
result = 21
print(solution(board), result)

board = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]
result = 11
print(solution(board), result)

board = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]
result = 33
print(solution(board), result)

board = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
result = 18
print(solution(board), result)