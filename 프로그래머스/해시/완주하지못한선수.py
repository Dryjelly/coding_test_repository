def solution(participant, completion):
    answer = ''

    p_dict = dict()

    for p in participant:
        if p in p_dict: p_dict[p] += 1
        else: p_dict[p] =  1

    for c in completion:
        p_dict[c] -= 1
        if p_dict[c] == 0: del p_dict[c]
    
    answer = list(p_dict.keys())[0]

    return answer

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))