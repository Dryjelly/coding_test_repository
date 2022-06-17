def solution(board, aloc, bloc):
    move = [[-1,0],[1,0],[0,-1],[0,1]] # 상하좌우
    answer = -1

    def out_of_borad(loc):
        if loc[0]<0 or loc[1]<0 or loc[0]>=len(board) or loc[1]>=len(board[0]): return True
        return False

    def dfs_a(board, aloc, bloc, count): # 승패 여부, 이동 횟수 반환
        # 승패여부 판단, 상대->나 순서로 체크해야함
        if board[bloc[0]][bloc[1]] == 0: return [1, count-1] # 나의 승리, 이미 상대가 빠져있으므로 count-1
        if board[aloc[0]][aloc[1]] == 0: return [0, count] # 나의 패배, 같이있던 상대가 탈출했으므로 빠지게됨

        b_w = [] # 상대방 승리 여부
        b_c = [] # 상대방 이동 횟수

        # 움직이기, 상대가 이기는지 확인
        for m in move:
            new_loc = [aloc[0]+m[0], aloc[1]+m[1]]
            if out_of_borad(new_loc): continue
            board[aloc[0]][aloc[1]] = 0 # 발판 없애기

            w, c = dfs_b(board, new_loc, bloc, count+1)
            b_w.append(w); b_c.append(c)

            board[aloc[0]][aloc[1]] = 1 # 발판 복구

        if not b_w: # 내가 움직일 곳이 없음, 나의 패배
            return [0, count]

        if sum(b_w) == len(b_w): # 모든 경우 상대방이 승리, 즉 나의 패배
            return [0,max(b_c)] # 최대 이동 횟수로 져야함
        if sum(b_w) == 0: # 모든 경우 상대방이 패배, 즉 나의 승리
            return [1,min(b_c)] # 최소 이동 횟수로 이겨야함

        # 최대한 나에게 유리한 선택하기
        # 상대방이 패배한 경우 중 최소 이동 횟수 선택
        min_c = 9999
        for w, c in zip(b_w, b_c):
            if w == 0: min_c = min(min_c, c)
        return [1,min_c]


    def dfs_b(board, aloc, bloc, count):
        # 승패여부 판단
        if board[aloc[0]][aloc[1]] == 0: return [1, count-1] # 나의 승리
        if board[bloc[0]][bloc[1]] == 0: return [0, count] # 나의 패배

        a_w = [] # 상대방 승리 여부
        a_c = [] # 상대방 이동 횟수

        # 움직이기
        for m in move:
            new_loc = [bloc[0]+m[0], bloc[1]+m[1]]
            if out_of_borad(new_loc): continue
            board[bloc[0]][bloc[1]] = 0 # 발판 없애기

            w, c = dfs_a(board, aloc, new_loc, count+1)
            a_w.append(w); a_c.append(c)

            board[bloc[0]][bloc[1]] = 1 # 발판 복구

        if not a_w: # 내가 움직일 곳이 없음, 나의 패배
            return [0, count]

        if sum(a_w) == len(a_w): # 모든 경우 상대방이 승리, 즉 나의 패배
            return [0,max(a_c)] # 최대 이동 횟수로 져야함
        if sum(a_w) == 0: # 모든 경우 상대방이 패배, 즉 나의 승리
            return [1,min(a_c)] # 최소 이동 횟수로 이겨야함

        # 최대한 나에게 유리한 선택하기
        # 상대방이 패배한 경우 중 최소 이동 횟수 선택
        min_c = 9999
        for w, c in zip(a_w, a_c):
            if w == 0: min_c = min(min_c, c)
        return [1,min_c]

    _, answer = dfs_a(board,aloc,bloc,0)

    return answer

print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]],
[1, 0],[1, 2]),5)

print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]],
[1, 0],[1, 2]),4)

print(solution([[1, 1, 1, 1, 1]],
[0, 0],[0, 4]),4)

print(solution([[1]],
[0, 0],[0, 0]),0)