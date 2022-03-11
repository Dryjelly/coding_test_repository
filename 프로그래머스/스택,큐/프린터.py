from collections import deque

def solution(priorities, location):
    answer = 0

    priorities_list = [0 for _ in range(10)]
    for p in priorities: priorities_list[p] += 1

    q = deque(priorities)
    counter = 0

    while(q):
        j = q.popleft()
        print_out = True
        for i in range(j+1,10):
            # 우선 순위가 더 높은 것이 존재함
            if priorities_list[i]:
                print_out = False
                break
        
        if print_out: # 인쇄하기
            counter += 1
            priorities_list[j] -= 1
            if location == 0: return counter
        else: # 대기 목록으로
            q.append(j)
        location -= 1
        if location == -1: location = len(q)-1

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))