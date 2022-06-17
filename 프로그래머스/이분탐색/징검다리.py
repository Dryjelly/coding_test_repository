def solution(distance, rocks, n):
    answer = 0

    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance

    while(left<=right):
        mid = (left + right)//2

        remove = 0
        prev = 0
        for r in rocks:
            if r-prev < mid: # 가장 작아야 하는 거리보다 작으면
                remove += 1 # 삭제
                if remove > n: break# 삭제 가능한 돌 개수 초과
            else: # 같거나 크면
                prev = r # 유지
        
        if remove > n: # 작아야 하는 거리 기준을 낮춰야 함
            right = mid-1
        else: # 거리 기준을 높여야 함
            left = mid+1
            answer = mid
        
    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))

print(solution(48,  [12, 25, 38, 43], 1))