def solution_1(board, skill):
    answer = 0

    for s in skill:
        s_type, r1, c1, r2, c2, degree = s
        m = 1
        if s_type == 1: m = -1
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):
                board[r][c] += degree * m

    print(board)
    for b in board:
        for i in b:
            if i>0: answer+=1

    return answer

def solution(board, skill):
    answer = 0
    new_board = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]

    for s in skill:
        s_type, r1, c1, r2, c2, degree = s
        cal = degree
        if s_type == 1: cal *= -1
        new_board[r1][c1] += cal
        new_board[r1][c2+1] += -cal
        new_board[r2+1][c1] += -cal
        new_board[r2+1][c2+1] += cal

    for r in range(len(board)):
        for c in range(1, len(board[0])):
            new_board[r][c] += new_board[r][c-1]
    
    for r in range(1, len(board)):
        for c in range(len(board[0])):
            new_board[r][c] += new_board[r-1][c]

    for r in range(len(board)):
        for c in range(len(board[0])):
            if new_board[r][c] + board[r][c] > 0: answer += 1
    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],
[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]), 10)

print(solution([[1,2,3],[4,5,6],[7,8,9]],
	[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]), 6)