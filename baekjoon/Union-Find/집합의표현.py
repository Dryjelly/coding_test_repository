import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())

num = [i for i in range(n+1)]

def find(a):
    if num[a] == a: return a
    else: 
        num[a] = find(num[a])
        return num[a]

def union(a, b):
    p_a = find(a)
    p_b = find(b)

    if p_a<p_b: num[p_b] = p_a
    else: num[p_a] = p_b

def check(a, b):
    if find(num[a]) == find(num[b]): print("YES"); return
    print("NO"); return


for i in range(m):
    c, a, b = map(int, input().split())
    if c == 0: union(a,b)
    else: check(a,b)

print(num)
