# from collections import deque
# def solution(prices):
#     answer = [0 for _ in range(len(prices))]
#     q = deque([])

#     for i, p in enumerate(prices):
#         q_len = len(q)
#         for _ in range(q_len):
#             out_i, out = q.popleft()
#             answer[out_i] += 1
#             if out <= p: q.append((out_i, out))

#         q.append((i,p))

#     return answer

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = [] # index 가 저장됨

    for i, p in enumerate(prices):
        while(stack):
            s_i = stack[-1]
            if prices[s_i] <= p: # 가격이 떨어지지 않음
                break
            else: # 가격이 떨어짐
                answer[s_i] = i - s_i
                stack.pop()
        stack.append(i)

    for s_i in stack:
        answer[s_i] = len(prices) - s_i - 1

    return answer

print(solution([1, 2, 3, 2, 3]))