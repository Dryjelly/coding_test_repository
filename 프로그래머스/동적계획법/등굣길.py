def solution(n, m, puddles):
    answer = 0

    map_school = [[0 for j in range(m)]for i in range(n)]
    for p in puddles: map_school[p[0]-1][p[1]-1] = -1
    map_school[0][0] = 1
    print(map_school)

    for i in range(n):
        for j in range(m):
            if map_school[i][j] == -1 or (i == 0 and j == 0): continue

            left = 0; up = 0
            if i == 0: left = map_school[i][j-1]
            elif j == 0: up = map_school[i-1][j]
            else:
                left = map_school[i][j-1]
                up = map_school[i-1][j]
                if left == -1: left = 0
                if up == -1: up = 0

            map_school[i][j] = left + up

    print(map_school)
    answer = map_school[-1][-1]
    return answer%1000000007

m = 4
n = 3
puddles = [[1,2]]
print(solution(m,n,puddles), 4)