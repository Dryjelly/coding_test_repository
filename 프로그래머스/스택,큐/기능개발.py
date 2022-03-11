def solution(progresses, speeds):
    answer = []
    day_remain = [-((-100+p)//s) for p, s in zip(progresses, speeds)] # 올림을 구현하기 위한 편법
    print(day_remain)

    day = 0
    for d_r in day_remain:
        if d_r - day <= 0: # 이미 완료된 프로젝트
            answer[-1] += 1
        else: # 미 완료된 프로젝트
            answer.append(1)
            day = d_r

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))