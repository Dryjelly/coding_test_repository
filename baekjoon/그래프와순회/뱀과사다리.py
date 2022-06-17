from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [-1 for _ in range(101)]
sc = {}

# ladder
for _ in range(N):
    s, e = map(int, input().split())
    sc[s] = e

# snake
for _ in range(M):
    s, e = map(int, input().split())
    sc[s] = e

level = 1
board[1] = 0
q = deque([1])

while q:
    q_size = len(q)
    for q_s in range(q_size):
        start = q.popleft()
        if start == 100:
            print(level-1)
            q = []; break
        for num in range(1,7): # 주사위 던지기
            next = start+num
            board[next] = level
            if next in sc:
                next = sc[next]
                if board[next] < level: continue
                board[next] = level
            q.append(next)
            