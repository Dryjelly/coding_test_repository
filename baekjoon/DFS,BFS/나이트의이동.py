import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

next = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]
def BFS(c_y, c_x, d_y, d_x, I):
    q = deque([])
    visited = set()
    def check(y,x):
        if y>=I or x>=I or y<0 or x<0: return False
        return True
    q.append((c_y, c_x))
    visited.add((c_y, c_x))
    step = 0
    while q:
        level = len(q)
        for _ in range(level):
            y, x = q.popleft()
            if (y, x) == (d_y, d_x): print(step); return
            for n in next:
                if check(y+n[0], x+n[1]) and (y+n[0], x+n[1]) not in visited:
                    q.append((y+n[0], x+n[1]))
                    visited.add((y+n[0], x+n[1]))
        step += 1

for t in range(T):
    I = int(input())
    c_y, c_x = map(int, input().split())
    d_y, d_x = map(int, input().split())
    BFS(c_y, c_x, d_y, d_x, I)