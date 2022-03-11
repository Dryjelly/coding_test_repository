def solution(id_list, report, k):
    answer = []
    report_name = {name : set() for name in id_list}
    report_num = {name : 0 for name in id_list}
    

    for r in report:
        u_id, r_id = r.split()
        check_l = len(report_name[u_id])
        report_name[u_id].add(r_id)
        if check_l != len(report_name[u_id]): report_num[r_id] += 1

    print(report_name)
    print(report_num)

    for name, r_names in report_name.items():
        num = 0
        print(name, r_names)
        for r_n in r_names:
            if report_num[r_n] >= k: num += 1
        answer.append(num)

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"],
["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
2))

print(solution(["con", "ryan"],
["ryan con", "ryan con", "ryan con", "ryan con"],
3))