import sys
import heapq
input = sys.stdin.readline

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

if N == 1: print(0); sys.exit()
if N < 3: print(sum(cards)); sys.exit()


answer = heapq.heappop(cards) + heapq.heappop(cards)
heapq.heappush(cards, answer)

while len(cards) != 1:
    cal = heapq.heappop(cards) + heapq.heappop(cards)
    answer += cal
    heapq.heappush(cards, cal)
print(answer)