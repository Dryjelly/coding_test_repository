def solution(citations):
    answer = 0
    
    paper_num = len(citations)
    citations.sort()

    for i in range(paper_num):
        if paper_num - i <= citations[i]: # 현재 논문의 인용수가 현재 논문을 포함한 남은 논문 개수 이상
            answer = paper_num - i
            break

    print(citations)

    return answer

print(solution([3, 0, 6, 1, 5])) # 3
print(solution([999])) # 0
print(solution([1])) # 1
print(solution([999,999,999])) # 0
print(solution([3, 2, 4, 1, 5])) # 3
print(solution([1, 888, 5, 5, 5])) # 3