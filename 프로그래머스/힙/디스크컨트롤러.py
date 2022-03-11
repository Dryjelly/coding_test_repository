import heapq

# def solution(jobs):
#     time = 0
#     heap = []
#     job_id = 0
#     while(len(jobs) != job_id):
#         while(len(jobs) != job_id and jobs[job_id][0] <= time): # 넣을 수 있는 작업을 힙에 넣기
#             heapq.heappush(heap, jobs[job_id][1])
#             job_id += 1
#         if not heap and len(jobs) != job_id:# 힙이 비어있지만 작업이 남아있다면
#             heapq.heappush(heap, jobs[job_id][1])
#             time = jobs[job_id][0]
#             job_id += 1

#         duration = heapq.heappop(heap)
#         time += duration

#     return time

def solution(jobs):
    answer = 0
    time = 0
    job_id = 0
    heap = []
    jobs.sort()

    while(len(jobs) != job_id):
        while(len(jobs) != job_id and jobs[job_id][0] <= time): # 넣을 수 있는 모든 작업을 힙에 넣기
            heapq.heappush(heap, jobs[job_id][::-1])
            job_id += 1
        if not heap and len(jobs) != job_id:# 힙이 비어있지만 작업이 남아있다면
            heapq.heappush(heap, jobs[job_id][::-1])
            time = jobs[job_id][0]
            job_id += 1
        
        duration, start = heapq.heappop(heap)
        answer += time - start + duration
        time += duration

    while(heap): # 힙에 존재하는 나머지 작업 수행
        duration, start = heapq.heappop(heap)
        answer += time - start + duration
        time += duration

    return answer//len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 3], [1, 9], [500, 6]]))