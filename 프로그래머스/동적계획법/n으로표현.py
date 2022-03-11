def solution(N, number):
    if N==number: return 1
    N_list = [set() for _ in range(8)]
    N_list[0].add(N)
    
    def cal_N(i):
        number = ''
        for _ in range(i+1): number += '1'
        return int(number)*N

    for i in range(1,8):
        N_list[i].add(cal_N(i))
        for c in range(1, ((i+1)//2)+1):
            c_1, c_2 = 0+c, i+1-c

            for n1 in N_list[c_1-1]:
                for n2 in N_list[c_2-1]:
                    if n1 == 0 or n2 == 0: continue
                    N_list[i].add(n1+n2)
                    N_list[i].add(n1-n2)
                    N_list[i].add(n1*n2)
                    N_list[i].add(n1//n2)
                    N_list[i].add(n2-n1)
                    N_list[i].add(n2//n1)

        print(N_list)
        if number in N_list[i] : return i+1

    return -1

print(solution(5,12), 4)
print(solution(2,11), 3)
print(solution(5,5), 1)
print(solution(8, 53),5)