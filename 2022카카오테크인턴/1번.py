# 성격지표
def solution(survey, choices):
    answer = ''

    p_dict = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    s_list = [['R','T'],['C','F'],['J','M'],['A','N']]
    num = [[],[3,0],[2,0],[1,0],[0,0],[0,1],[0,2],[0,3]]

    for i, c in enumerate(choices):
        p_dict[survey[i][0]] += num[c][0]
        p_dict[survey[i][1]] += num[c][1]

    print(p_dict)

    for s in s_list:
        if p_dict[s[0]] >= p_dict[s[1]]:
            answer+=s[0]
        else:
            answer+=s[1]

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])) # TCMA
print(solution(["TR", "RT", "TR"], [7, 1, 3])) # RCJA
