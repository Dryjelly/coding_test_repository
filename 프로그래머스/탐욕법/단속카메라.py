import heapq

def solution_1(routes):
    answer = 0
    routes.sort()
    
    end_point = []

    for s, e in routes:
        heapq.heappush(end_point, e)
        if s == end_point[0]:
            answer += 1
            end_point = []
        elif s > end_point[0]:
            answer += 1
            end_point = []
            heapq.heappush(end_point, e)
            
    if end_point: answer += 1

    return answer

def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    
    last_cam = -30001

    for s, e in routes:
        if s > last_cam:
            answer += 1
            last_cam = e

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2

print(solution([[-20,-8], [-20,-15], [-14,-5], [-18,-13], [-5,-3], [-17,-16]])) #2