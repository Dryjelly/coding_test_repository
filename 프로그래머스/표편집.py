def solution(n, k, cmd):
    answer = ''
    table = [1 for _ in range(n)]
    near = [[i-1, i+1] for i in range(n)]
    stack = []

    for c in cmd:
        if c[0] == 'D':
            cnt = int(c[2:])
            for i in range(cnt):
                k = near[k][1]
            
        elif c[0] == 'U':
            cnt = int(c[2:])
            for i in range(cnt):
                k = near[k][0]

        elif c[0] == 'C':
            table[k] = 0
            stack.append(k)
            if near[k][0] == -1:
                near[near[k][1]][0] = -1
                k = near[k][1]

            elif near[k][1] == n:
                near[near[k][0]][1] = n
                k = near[k][0]

            else:
                near[near[k][0]][1] = near[k][1]
                near[near[k][1]][0] = near[k][0]
                k = near[k][1]

        else: # 'Z'
            temp = stack.pop()
            table[temp] = 1
            front = near[temp][0]
            back = near[temp][1]

            if front != -1: near[front][1] = temp
            if back != n: near[back][0] = temp

    for t in table:
        if t:
            answer += 'O'
        else:
            answer += 'X'
    return answer

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print("OOOOXOOO")
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
print(solution(8,2,["C","C","C","C","C","C","C","Z","Z","Z","Z","Z","Z","Z"]))
print("OOXOXOOO")