import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
k = int(input())
num = [input().rstrip() for _ in range(n)]
num_set = set()

for com in permutations(num, k):
    num_set.add("".join(com))

print(len(num_set))

