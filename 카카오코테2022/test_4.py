def solution(n, info):
    answer = [0 for _ in range(11)]
    cost = [] # 가치, 필요한 화살 개수
    score_a = 0

    for i, num in enumerate(info[::-1]):
        if i == 0 : num = 0
        if num != 0 :
            cost.append((2*i, num+1))
            score_a += i
        else :
            cost.append((i, num+1))
            
    # print(score_a)

    max_score = [-score_a, []] # 점수 차이, 맞춘 점수
    v = [[-score_a for _ in range(n+1)] for _ in range(11)]
    v_s = [[[] for _ in range(n+1)] for _ in range(11)]
    
    # print(v)
    # print(v_s)
    # print(cost)

    for s in range(1, 11):
        for a in range(1, n+1):
            # 현재 점수에 필요한 화살 개수가 충분함
            if a >= cost[s][1]:
                if v[s-1][a] < cost[s][0] + v[s-1][a-cost[s][1]]:
                    v[s][a] = cost[s][0] + v[s-1][a-cost[s][1]]
                    v_s[s][a] = v_s[s-1][a-cost[s][1]] + [s]
                else: # 같을 때 여기서도 비교해야 할듯!!!!!! v_s[s][a] 이거
                    v[s][a] = v[s-1][a]
                    v_s[s][a] = v_s[s-1][a]
            # 모자람
            else:
                v[s][a] = v[s-1][a]
                v_s[s][a] = v_s[s-1][a]

            if v[s][a] > max_score[0]:
                max_score[0] = v[s][a]
                max_score[1] = v_s[s][a]
            elif v[s][a] == max_score[0] and max_score[1] != v_s[s][a]:

                temp_1 = [0 for _ in range(11)] # 기존
                temp_2 = [0 for _ in range(11)] # 비교할 거

                check = 0
                for t_s in max_score[1]:
                    temp_1[t_s] = cost[t_s][1]
                    check += cost[t_s][1]
                if check != n: temp_1[0] = n-check

                check = 0
                for t_s in v_s[s][a]:
                    temp_2[t_s] = cost[t_s][1]
                    check += cost[t_s][1]
                if check != n: temp_2[0] = n-check

                # 비교 해야됨
                for t_1,t_2 in zip(temp_1, temp_2):
                    if t_1 > t_2: break
                    elif t_1 < t_2: max_score[1] = v_s[s][a]; break


    # print(v)
    # print(v_s)
    # print(max_score)

    if max_score[0] <= 0: return [-1]

    check = 0
    for s in max_score[1]:
        answer[s] = cost[s][1]
        check += cost[s][1]

    if check != n: answer[0] = n-check

    return answer[::-1]


print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))
print(solution(3,[0,0,0,0,0,0,0,0,0,0,3]))