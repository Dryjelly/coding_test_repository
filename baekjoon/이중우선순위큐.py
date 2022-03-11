import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def solution(operations):
    answer = []
    num_dict = defaultdict(int)
    min_heap = []
    max_heap = []
    for o in range(operations):
        oper, num = input().split()
        num = int(num)
        if oper == 'I':
            num_dict[num] += 1
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif oper == 'D':
            if num == 1:
                while(max_heap and num_dict[-max_heap[0]] == 0): heapq.heappop(max_heap)
                if not max_heap: continue
                else:
                    max_num = -heapq.heappop(max_heap)
                    num_dict[max_num] -= 1
            elif num == -1:
                while(min_heap and num_dict[min_heap[0]] == 0): heapq.heappop(min_heap)
                if not min_heap: continue
                else:
                    min_num = heapq.heappop(min_heap)
                    num_dict[min_num] -= 1
            # if num == 1:
            #     while(max_heap):
            #         max_num = -heapq.heappop(max_heap)
            #         if num_dict[max_num] != 0:
            #             num_dict[max_num] -= 1
            #             break
            # elif num == -1:
            #     while(min_heap):
            #         min_num = heapq.heappop(min_heap)
            #         if num_dict[min_num] != 0:
            #             num_dict[min_num] -= 1
            #             break
    
    while(max_heap and num_dict[-max_heap[0]] == 0): heapq.heappop(max_heap)
    while(min_heap and num_dict[min_heap[0]] == 0): heapq.heappop(min_heap)

    if not max_heap: print('EMPTY')
    else: print(-max_heap[0], min_heap[0])

T = int(input())
print(T)
for _ in range(T):
    k = int(input())
    solution(k)