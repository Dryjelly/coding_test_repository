from collections import deque
from itertools import permutations

def card_cost(board, cur_loc, dist_loc):
    #BFS
    cost = [[999]*4 for _ in range(4)] # max_value = 999
    visited = [[False]*4 for _ in range(4)]
    q = deque([[cur_loc, 0]]) # loc, cur_cost
    move_r = [-1, 1, 0, 0] # 상, 하, 좌, 우
    move_c = [0, 0, -1, 1]

    while q:
        (r, c), cur_cost = q.popleft()

        visited[r][c] = True
        #if (r, c) == dist_loc: return cur_cost+1 # 목표 위치 도착
        if cost[r][c] > cur_cost: cost[r][c] = cur_cost
        else: continue

        for i in range(4): # 4방향으로 움직임
            next_r, next_c = r+move_r[i], c+move_c[i]

            # 한번만 움직임 --------------------------------
            if next_r < 0 or next_r >= 4 or next_c < 0 or next_c >= 4: continue # 밖으로 나가면 고려 안함
            if visited[next_r][next_c] : continue # 방문한 곳이면 고려 안함
            q.append([(next_r, next_c), cur_cost + 1])
            if board[next_r][next_c] != 0: continue # 현재 위치에 카드가 있다면 ctrl 고려 안함
            # ---------------------------------------------

            # ctrl 누르고 움직임 ---------------------------
            while(True): # 한칸씩 계속 이동
                nnext_r, nnext_c = next_r+move_r[i], next_c+move_c[i]
                if nnext_r < 0 or nnext_r >= 4 or nnext_c < 0 or nnext_c >= 4: break # 밖으로 나간다면 종료함
                next_r, next_c = nnext_r, nnext_c
                if board[next_r][next_c] != 0: break # 카드를 만나면 종료

            if next_r == r+move_r[i] and next_c == c+move_c[i]: # 이동하지 않았다면 고려 안함
                continue
            if visited[next_r][next_c] : continue # 방문한 곳이면 고려 안함
                
            q.append([(next_r, next_c), cur_cost + 1])
            # --------------------------------------------

    return cost[dist_loc[0]][dist_loc[1]]+1

def total_cost(board, card, card_order, cur_loc, idx, cost):
    if len(card_order) == idx: return cost # 모두 계산됨

    card_num = card_order[idx]

    card_A_loc = card[card_num][0]
    card_B_loc = card[card_num][1]

    # print(f'card_order = {card_order}\nnow = {card_order[idx]}')

    # print('board---------------')
    # for bc in board: print(bc)
    # print('--------------------')

    # print(f'prev_loc = {cur_loc} -> card_A_loc = {card_A_loc} / card_B_loc = {card_B_loc}')
    # print(f'prev -> A = {card_cost(board, cur_loc, card_A_loc)} -> B = {card_cost(board, card_A_loc, card_B_loc)}')
    # print(f'prev -> B = {card_cost(board, cur_loc, card_B_loc)} -> A = {card_cost(board, card_B_loc, card_A_loc)}')

    cost_A_B = cost + card_cost(board, cur_loc, card_A_loc)+card_cost(board, card_A_loc, card_B_loc) # 현재위치 -> A 카드로 -> B 카드로
    cost_B_A = cost + card_cost(board, cur_loc, card_B_loc)+card_cost(board, card_B_loc, card_A_loc) # 현재위치 -> B 카드로 -> A 카드로

    # print(f'cost_A_B = {cost_A_B}, cost_B_A = {cost_B_A}\n')

    # 선택된 카드 없애기
    board[card_A_loc[0]][card_A_loc[1]] = 0
    board[card_B_loc[0]][card_B_loc[1]] = 0

    cost_A = total_cost(board, card, card_order, card_B_loc, idx+1, cost_A_B)
    cost_B = total_cost(board, card, card_order, card_A_loc, idx+1, cost_B_A)

    # 선택된 카드 복구
    board[card_A_loc[0]][card_A_loc[1]] = card_num
    board[card_B_loc[0]][card_B_loc[1]] = card_num

    return min(cost_A, cost_B)

def solution(board, cursor_r, cursor_c):
    answer = 0
    card = {}    # 카드 위치 저장
    card_num = 0 # 카드 개수
    for r in range(4):
        for c in range(4):
            if board[r][c] != 0:
                if board[r][c] not in card.keys():
                    card[board[r][c]] = [(r,c)]
                    if card_num < board[r][c]: card_num = board[r][c]
                else : 
                    card[board[r][c]].append((r,c))
                    
    min_cost = 999999999
    for card_order in permutations(list(range(1, card_num+1)), card_num):
        cost = total_cost(board, card, card_order, (cursor_r, cursor_c), 0, 0)
        min_cost = min(min_cost, cost)

    return min_cost

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
answer = 14

board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
r = 0
c = 1
answer = 16

print(solution(board, r, c), answer)