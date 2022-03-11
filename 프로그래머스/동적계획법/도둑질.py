def solution(money):
    answer = 0
    if len(money) == 3: return max(money[0], money[1], money[2])
    answer = max(money[0], money[1], money[2]+money[0])

    # 첫 집 털기
    money_rob = [money[0], money[1], money[2]+money[0]] + [0 for _ in range(len(money) - 3)]
    for i in range(3,len(money)-1):
        money_rob[i] = max(money_rob[i-2], money_rob[i-3]) + money[i]
        answer = max(answer, money_rob[i])

    # 첫 집 안털기
    money_rob = [0, money[1], money[2]] + [0 for _ in range(len(money) - 3)]
    for i in range(3,len(money)):
        money_rob[i] = max(money_rob[i-2], money_rob[i-3]) + money[i]
        answer = max(answer, money_rob[i])

    return answer

    money_rob = [[money[0], 0, 0, 0, 0, 0],
                 [money[1], money[0], money[1], 0, 0, 0],
                 [money[2]+money[0], max(money[1], money[0]), money[2], money[1], money[2], 0],]

    # print(money_rob)
    for m in range(3,len(money)-1):
        temp = [money[m] + money_rob[m-1][1], max(money_rob[m-1][0], money_rob[m-1][1]),
                money[m] + money_rob[m-1][3], max(money_rob[m-1][2], money_rob[m-1][3]),
                money[m] + money_rob[m-1][5], max(money_rob[m-1][4], money_rob[m-1][5]),]
        money_rob.append(temp)
    
    temp = [money_rob[-1][0], money_rob[-1][1],
            money[-1] + money_rob[-1][3], max(money_rob[-1][2], money_rob[-1][3]),
            money[-1] + money_rob[-1][5], max(money_rob[-1][4], money_rob[-1][5]),]
    money_rob.append(temp)

    # print(money_rob)
    answer = max(money_rob[-1])

    return answer

    for i in range(3):
        if i == 0: money_new = money[i:-1]
        else: money_new = money[i:]
        # money_new = money[i:]# + money[:i]
        # money_new = money_new[:-1]
        money_rob = [[0,0] for _ in range(len(money_new))]
        money_rob[0][0] = money_new[0]

        print(money_new, money_rob)

        for m in range(1, len(money_new)):
            money_rob[m][0] = money_new[m] + money_rob[m-1][1]
            money_rob[m][1] = max(money_rob[m-1][0], money_rob[m-1][1])

        print(money_new, money_rob)
        answer = max(answer, money_rob[-1][0], money_rob[-1][1])
    
    return answer

    rob_first = [False for _ in range(len(money))]
    rob_first[0] = True
    rob_first[2] = True
    money[2] += money[0]

    answer = max(money[0], money[1], money[2])

    for i in range(3, len(money)-1):
        if money[i-2] > money[i-3]:
            money[i] += money[i-2]
            rob_first[i] = rob_first[i-2]

        elif  money[i-2] < money[i-3]:
            money[i] += money[i-3]
            rob_first[i] = rob_first[i-3]

        else: 
            if rob_first[i-2] == False:
                money[i] += money[i-2]
            elif rob_first[i-3] == False:
                money[i] += money[i-3]
            else:
                money[i] += money[i-2]
                rob_first[i] = True
        
        answer = max(answer, money[i])

    m3 = money[-3]
    m4 = money[-4]
    if rob_first[-3] == True: m3 -= money[0]
    if rob_first[-4] == True: m4 -= money[0]

    if m3 > m4:
        money[-1] += m3
    elif  m3 < m4:
        money[-1] += m4

    answer = max(answer, money[-1])

    return answer

print(solution([1,2,3,1]), 4)
print(solution([1,1,4,1,4]), 8)
print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000)
print(solution([1000,1,0,1,2,1000,0]), 2001)
print(solution([1000,0,0,0,0,1000,0,0,0,0,0,1000]), 2000)
print(solution([1,2,3,4,5,6,7,8,9,10]), 30)
print(solution([0,0,0,0,100,0,0,100,0,0,1,1]), 201)
print(solution([11,0,2,5,100,100,85,1]), 198)
print(solution([1,2,3]), 3)
print(solution([91,90,5,7,5,7]), 104)
print(solution([90,0,0,95,1,1]), 185)