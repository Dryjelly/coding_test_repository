def solution(board):
    answer = 0

    def is_available(loc, num):
        pass

    def DFS(loc, num):
        move = [(0,-1),(0,1),(-1,0),(1,0)]
        global x,y
        x, y = (loc[0],loc[0]), (loc[1],loc[1])

        def dfs(loc):
            if board[loc[0]][loc[1]] != num: return
            board[loc[0]][loc[1]] *= -1
            global x,y
            x = (min(x[0],loc[0]),max(x[1],loc[0]))
            y = (min(y[0],loc[1]),max(y[1],loc[1]))
            for m in move:
                next_loc = (loc[0]+m[0], loc[1]+m[1])
                if next_loc[0] < 0 or next_loc[1] < 0 or next_loc[0] >= len(board) or next_loc[1] >= len(board[0]):
                    continue
                dfs(next_loc)

        dfs(loc)

        check = [False for _ in range(y[0],y[1]+1)]
        for i in range(x[0],x[1]+1):
            for j in range(y[0],y[1]+1):
                if check[j] == True: continue
                if board[i][j] == -num:
                    for x_c in range(i,x[1]+1):
                        if board[x_c][j] != -num




        print(x,y)

    

    visited = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0 and board[i][j] not in visited:
                visited.add(-board[i][j])
                DFS((i,j), board[i][j])
    print(board)
    return answer

print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))
#2