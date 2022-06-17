# 큐 합 같게
from collections import deque
def solution(queue1, queue2):
    answer = 0

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    total = q1_sum + q2_sum

    if total%2 != 0: return -1 # 나눌 수 없음
    target = total//2

    print(q1_sum, q2_sum, total)

    while(q1_sum != q2_sum):
        if q1_sum >= q2_sum:
            num = queue1.popleft()
            queue2.append(num)
            q1_sum -= num
            q2_sum += num
        else:
            num = queue2.popleft()
            queue1.append(num)
            q1_sum += num
            q2_sum -= num
    
        answer += 1
        if answer > (len(queue1) + len(queue2))*2: answer=-1;break

    return answer

print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2])) # 7
print(solution([1, 1], 	[1, 5])) # -1
print(solution([3,1,1,5], [5,1,1,7])) # -1