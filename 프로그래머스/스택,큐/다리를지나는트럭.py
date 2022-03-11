from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     q = deque([0 for _ in range(bridge_length)])
#     remain_weight = weight
#     left_truck_weight = 0

#     truck_weights_list = [0 for _ in range(10000)]
#     for tw in truck_weights:
#         truck_weights_list[tw] += 1
#         left_truck_weight += tw

#     # truck_weights.sort()
#     # print(truck_weights)

#     while(left_truck_weight):
#         answer += 1
#         out = q.popleft() # 다리 위 트럭 내보내기
#         remain_weight += out
#         left_truck_weight -= out

#         for i in range(remain_weight, -1, -1): # 트럭 리스트 확인
#             if truck_weights_list[i]: # 알맞은 트럭 존재함
#                 truck_weights_list[i] -= 1
#                 remain_weight -= i
#                 q.append(i)
#                 break
        
#         if len(q) != bridge_length: q.append(0) # 못들어감

#         # for i in range(len(truck_weights)-1,-1,-1): # 트럭 리스트 확인
#         #     if remain_weight - truck_weights[i] >= 0: # 남는 자리 있으면
#         #         remain_weight -= truck_weights[i]
#         #         q.append(truck_weights[i])


#     return answer

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_q = deque([0 for _ in range(bridge_length)])
    truck_num = 0

    remain_weight = weight

    while(truck_num != len(truck_weights)):
        answer += 1
        out = bridge_q.popleft() # 다리 위 트럭 내보내기
        remain_weight += out

        if remain_weight - truck_weights[truck_num] >= 0: # 남는 자리 있으면
            remain_weight -= truck_weights[truck_num]
            bridge_q.append(truck_weights[truck_num])
            truck_num += 1
        else: # 자리 없음
            bridge_q.append(0)

    return answer+bridge_length

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))