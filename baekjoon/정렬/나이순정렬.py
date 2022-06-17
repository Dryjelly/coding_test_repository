import sys
# import heapq
# from collections import deque, defaultdict
# from itertools import permutations, combinations

input = sys.stdin.readline

# name_list = [[] for _ in range(201)]

# N = int(input())

# for _ in range(N):
#     age, name = input().split()
#     name_list[int(age)].append(name)

# for age, names in enumerate(name_list):
#     for name in names:
#         print(age, name)


N = int(input())

n_list = []

for n in range(N):
    age, name = input().split()
    n_list.append((int(age), name))

n_list.sort(key=lambda x:x[0])
for age, name in n_list:
    print(age, name)