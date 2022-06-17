import sys
from itertools import combinations

input = sys.stdin.readline

N,M = map(int, input().split())

card = [i for i in map(int, input().split())]
max_value = 0
for i in combinations(card,3):
    temp = sum(i)
    if M >= temp and max_value < temp:
        max_value = temp

print(max_value)