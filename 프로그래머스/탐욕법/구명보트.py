def solution_v1(people, limit):
    answer = 0

    weight_list = [0 for _ in range(241)]
    weight_set = set()
    weight_set_2 = set()

    for p in people:
        if limit-p < 40: answer += 1
        else:
            weight_list[p] += 1
            weight_set.add(p)

    for w1 in weight_set:
        if w1 in weight_set_2: continue # 삭제됐으면 건너뛰기
        for w2 in range(limit-w1, 39, -1): # 사람 찾기
            if weight_list[w2] > 0:
                if w1 == w2: # 같은무게 걸림
                    answer += weight_list[w1]//2
                    if weight_list[w1]%2 == 0: # 짝수면
                        weight_list[w1] = 0
                        weight_set_2.add(w1)
                        break # 끝, 다른사람 구출
                    else: # 홀수면
                        weight_list[w1] = 1 # 소비하기 위해 for문 탐색
                elif weight_list[w1] > weight_list[w2]: # w1 이 더 많음
                    answer += weight_list[w2]
                    weight_list[w1] -= weight_list[w2]
                    weight_list[w2] = 0
                    weight_set_2.add(w2) # w1 소비하기 위해 for문 탐색
                elif weight_list[w1] < weight_list[w2]: # w2 이 더 많음
                    answer += weight_list[w1]
                    weight_list[w2] -= weight_list[w1]
                    weight_list[w1] = 0
                    weight_set_2.add(w1)
                    break # 끝, 다른사람 구출
                elif weight_list[w1] == weight_list[w2]: # 같음
                    answer += weight_list[w1]
                    weight_list[w2] = 0
                    weight_set_2.add(w2)
                    weight_list[w1] = 0
                    weight_set_2.add(w1)
                    break # 끝, 다른사람 구출

    for w1 in weight_set-weight_set_2: # 남은사람 구출
        answer += weight_list[w1]

    return answer

def solution(people, limit):
    answer = 0

    people.sort()

    s = 0
    e = len(people)-1

    while(s<e):
        if people[s] + people[e] <= limit:
            answer += 1
            s += 1
        e -= 1

    return len(people) - answer

print(solution([70, 50, 80, 50],100),3)
print(solution([70, 80, 50],100),3)
print(solution([40,50,150,160],200),2)
print(solution([40,50,60,90],100),3)
print(solution([70, 50, 80, 50, 90, 40], 240), 3)

# print(solution([100,500,500,900,950],1000 ),3)