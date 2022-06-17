import sys
from collections import defaultdict

input = sys.stdin.readline

g, s = map(int, input().split())
W = input().rstrip()
S = input().rstrip()

w1_list = [0] * 58
w2_list = [0] * 58

for w in W: w1_list[ord(w) - 65] += 1

answer = 0
length = 0
start = 0

for i in range(s):
    w2_list[ord(S[i])-65] += 1
    length += 1

    if length == g:
        if w1_list == w2_list:
            answer += 1
        w2_list[ord(S[start])-65] -= 1
        length -= 1
        start += 1

print(answer)

# W_set = defaultdict(int)

# for w in W: W_set[w] += 1

# # print(W_set)

# answer = 0
# check = 0
# start = 0

# for i in range(g):
#     if S[i] in W_set:
#         if W_set[S[i]] > 0: check += 1
#         W_set[S[i]] -= 1
# if check == g: answer += 1

# for i in range(g, s):
#     if S[start] in W_set:
#         if W_set[S[start]] >= 0: check -= 1
#         W_set[S[start]] += 1
#     start += 1
#     if S[i] in W_set:
#         if W_set[S[i]] > 0: check += 1
#         W_set[S[i]] -= 1
#     if check == g: answer += 1

# print(answer)
