def solution(n, info):
    global answer, max_diff
    answer = [-1]
    R_list = [0] * 11
    max_diff = 0

    def cal_score(R_list): # 점수 계산
        score = 0
        for i in range(len(R_list)):
            if R_list[i]: score += 10-i
            elif info[i]: score -= 10-i
        return score

    def check_low_score(list_ori, list_new):
        for lo, ln in zip(list_ori[::-1], list_new[::-1]):
            if lo > ln: return list_ori
            elif lo < ln: return list_new
        return list_ori

    def dfs(idx, remain, R_list):
        global answer, max_diff

        if remain == 0 or idx == 10: # 화살을 다 썻거나 0 점에 버린다면
            R_list[10] = remain # 나머지 0 점에 버리기
            diff = cal_score(R_list)
            if diff > max_diff: # 점수 차이가 더 난다면
                # print(R_list,diff,max_diff,answer)
                max_diff = diff
                answer = R_list[:]
            elif diff == max_diff and diff != 0: # 점수 차이가 같으면
                answer = check_low_score(answer, R_list)[:]
                # print(R_list,diff,max_diff,answer)
            return

        # 선택
        if remain >= info[idx]+1: # 어피치 보다 1개 많으면 선택가능
            R_list[idx] = info[idx]+1
            dfs(idx+1, remain-info[idx]-1, R_list)

        # 선택 안함
        R_list[idx] = 0
        dfs(idx+1, remain, R_list)
        
    dfs(0,n,R_list)

    return answer

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))
print(solution(3,[0,0,0,0,0,0,0,0,0,0,3]))