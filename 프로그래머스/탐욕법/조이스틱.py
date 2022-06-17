def solution(name):
    if set(name) == {'A'}: return 0
    
    def change_word(word):
        move = ord(word)-ord('A')
        if move > 13: return 26-move
        else: return move

    def cal_remain(name_list):
        for i in range(len(name_list)): # cut A
            if name_list[i] == 'A':
                continue
            else:
                name_list = name_list[i:]
                break
        return len(name_list)
    
    answer = 0
    for n in name: answer += change_word(n)
    reverse_name = name[0] + name[-1:0:-1]
    # print(reverse_name)
    
    step = 999999
    for i in range(len(name)):
        # if name[i] == 'A':
        step = min(step, i*2 + cal_remain(name[i+1:]))
        # if reverse_name[i] == 'A':
        step = min(step, i*2 + cal_remain(reverse_name[i+1:]))

    if step == 999999: step = len(name) - 1

    return answer + step

print(solution("N")) # 13
print(solution("JAZ")) # 11
print(solution("JEROEN")) # 56
print(solution("JAN")) # 23

# answer += 12 - (cal%14) * (cal//14)