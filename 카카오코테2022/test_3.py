def solution(fees, records):
    answer = []

    times = {}

    def min_time(time):
        min = int(time[3:])
        min += int(time[:2]) * 60
        return min

    for rec in records:
        time, car_num, act = rec.split()
        if car_num not in times: times[car_num] = []
        times[car_num].append(min_time(time))

    times = sorted(times.items())
    print(times)

    for time in times:
        cost = fees[1]
        total_time = 0
        if len(time[1])%2 != 0: time[1].append(1439)
        for i in range(0,len(time[1]),2):
            total_time += time[1][i+1] - time[1][i]
        print(total_time)
        if total_time > fees[0]:
            cost += (total_time - fees[0])//fees[2] * fees[3]
            if (total_time - fees[0])%fees[2] != 0: cost += fees[3]
        answer.append(cost)

    return answer


print(solution([180, 5000, 10, 600],
["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

print(solution([120, 0, 60, 591],
["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))

print(solution([1, 461, 1, 10],
["00:00 1234 IN"]))
