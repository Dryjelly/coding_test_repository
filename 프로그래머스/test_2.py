# def solution(n):
#     answer = 1

#     cnt = 0
#     for i in range(1, n):
#         cnt += i
#         if ((n+cnt)%(i+1) == 0) and ((n+cnt)/(i+1) - i > 0): answer += 1

#     return answer

# print(solution(15))

def solution(citations):
    answer = citations
    answer.sort(reverse = True)
    for i, a in enumerate(answer):
        if a < i+1 : return i
    return i+1

print(solution([3, 0, 6, 1, 5]))
print(solution([100]))