#
def solution(alp, cop, problems):
    answer = 0

    solved = set()
    card = []
    
    oby_a = sorted(range(len(problems)), key=lambda x:problems[x][0])
    oby_c = sorted(range(len(problems)), key=lambda x:problems[x][1])

    print(oby_a, oby_c)

    def cal_time(i):
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[i]

        req_a = alp_req-alp
        req_c = cop_req-cop

        if 

        return 0


    return answer

print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]])) #15
print(solution(0,0,	[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]])) #13