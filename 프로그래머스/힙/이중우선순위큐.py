# def solution(operations):
#     answer = []
#     min_heap = []
#     max_heap = []
#     index_dict = {}

#     def swap(heap, index_1, index_2, mode):
#         index_dict[heap[index_1]][mode].remove(index_1)
#         index_dict[heap[index_2]][mode].remove(index_2)
#         index_dict[heap[index_1]][mode].add(index_2)
#         index_dict[heap[index_2]][mode].add(index_1)
#         heap[index_1], heap[index_2] = heap[index_2], heap[index_1]
        
#     def heapify(heap, index, mode):
#         small = index
#         left_index = 2*index+1
#         right_index = 2*index+2
#         if len(heap) > left_index and heap[left_index] < heap[small]:
#             small = left_index
#         if len(heap) > right_index and heap[right_index] < heap[small]:
#             small = right_index
#         if small != index:
#             swap(heap, index, small, mode)
#             heapify(heap, small, mode)
#     def insert_heap(heap, num, mode):
#         heap.append(num)
#         index = len(heap)-1
#         index_dict[num][mode].add(index)
#         while 0 < index:
#             parent_index = (index-1)//2
#             if heap[parent_index] > heap[index]:
#                 swap(heap, parent_index, index, mode)
#                 index = parent_index
#             else: break
#     def pop_heap(heap, mode):
#         min_value = heap[0]
#         last_index = len(heap)-1
#         if last_index != 0: swap(heap, 0, last_index, mode)
#         del heap[-1]
#         index_dict[min_value][mode].remove(last_index)
#         if last_index != 0: heapify(heap, 0, mode)
#         return min_value
#     def value_remove(heap, value, mode):
#         index = list(index_dict[value][mode])[0]
#         while 0 < index:
#             parent_index = (index-1)//2
#             swap(heap, parent_index, index, mode)
#             index = parent_index
#         return pop_heap(heap, mode)

#     for o in operations:
#         oper, num = o.split()
#         if oper == 'I':
#             if int(num) not in index_dict: index_dict[int(num)] = [set([]), set([])]
#             if -int(num) not in index_dict: index_dict[-int(num)] = [set([]), set([])]
#             insert_heap(min_heap, int(num), 0)
#             insert_heap(max_heap, -int(num), 1)
#         else:
#             if not min_heap: continue
#             if num == '1':
#                 max_value = pop_heap(max_heap, 1)
#                 _ = value_remove(min_heap, -max_value, 0)
#             else:
#                 min_value = pop_heap(min_heap, 0)
#                 _ = value_remove(max_heap, -min_value, 1)

#     # print(max_heap, min_heap)
#     if len(min_heap) == 0 or len(max_heap) == 0 : answer = [0,0]
#     else: answer = [-max_heap[0], min_heap[0]]
#     return answer

import heapq
from collections import defaultdict

def solution(operations):
    answer = []
    num_dict = defaultdict(int)
    min_heap = []
    max_heap = []
    for o in operations:
        oper, num = o.split()
        num = int(num)
        if oper == 'I':
            num_dict[num] += 1
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif oper == 'D':
            if num == 1:
                while(max_heap):
                    max_num = -heapq.heappop(max_heap)
                    if num_dict[max_num] != 0:
                        num_dict[max_num] -= 1
                        break
            elif num == -1:
                while(min_heap):
                    min_num = heapq.heappop(min_heap)
                    if num_dict[min_num] != 0:
                        num_dict[min_num] -= 1
                        break
    
    while(max_heap and num_dict[-max_heap[0]] == 0): heapq.heappop(max_heap)
    while(min_heap and num_dict[min_heap[0]] == 0): heapq.heappop(min_heap)

    if not max_heap: answer = [0,0]
    else: answer = [-max_heap[0], min_heap[0]]
            
    return answer

print(solution(["I 16","D 1"])) # 00
print(solution(["I 7","I 5","I -5","D -1"])) # 75
print(solution(["I 2","I 4","D -1", "I 1", "D 1"])) # 11
print(solution(["I 3", "I 2", "I 1", "D 1", "D 1", "I 3", "D -1"])) #33
print(solution(["I 6", "I 2", "I 1", "I 4", "I 5", "I 3", "D 1", "I 7", "D -1", "I 6", "D -1", "D -1"])) #74