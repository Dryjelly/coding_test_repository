import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    print(scoville)

    while(scoville[0] < K):
        if len(scoville) == 1: return -1
        out_1 = heapq.heappop(scoville)
        out_2 = heapq.heappop(scoville)
        heapq.heappush(scoville, out_1 + out_2 * 2)
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))