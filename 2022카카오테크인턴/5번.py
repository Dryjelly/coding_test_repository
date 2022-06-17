from collections import deque
def solution(rc, operations):
    answer = [[]]
    
    rc = deque(rc)
    for i in range(len(rc)):
        rc[i] = deque(rc[i])

    def sr(rc):
        rc.appendleft(rc.pop())

    def ro(rc):

        for i in range(len(rc)):
            if i != len(rc)-1: cur_num = rc[i].pop() # 마지막 숫자

            if i != 0:# 아래것 뽑아 나한테 주기
                rc[i].append(prev_num) # 넣기
                
            if i != len(rc)-1:# 위것 뽑아 나한테 주기
                rc[i].appendleft(rc[i+1].popleft())
            
            prev_num = cur_num # 이전 마지막 숫자가 됨


    for o in operations:
        if o == "Rotate":
            ro(rc)
        else:
            sr(rc)

    for i in range(len(rc)):
        rc[i] = list(rc[i])
    rc = list(rc)

    return rc

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]],["Rotate", "ShiftRow"]),[[8, 9, 6], [4, 1, 2], [7, 5, 3]])
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]],["Rotate", "ShiftRow", "ShiftRow"]),[[8, 3, 3], [4, 9, 7], [3, 8, 6]])
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],["ShiftRow", "Rotate", "ShiftRow", "Rotate"]),[[1, 6, 7 ,8], [5, 9, 10, 4], [2, 3, 12, 11]])