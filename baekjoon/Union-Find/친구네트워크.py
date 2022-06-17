import sys
input = sys.stdin.readline

def find(friend, name):
    if friend[name] == name: return name
    friend[name] = find(friend, friend[name])
    return friend[name]

def union(friend, connect, f1, f2):
    p_f1 = find(friend, f1)
    p_f2 = find(friend, f2)

    if p_f1 == p_f2: return
    friend[p_f2] = p_f1
    connect[p_f1] += connect[p_f2]
    

T = int(input())
for t in range(T):

    friend = {}
    connect = {}

    K = int(input())
    for k in range(K):
        f1, f2 = input().split()
        if f1 not in friend:
            friend[f1] = f1
            connect[f1] = 1
        if f2 not in friend:
            friend[f2] = f2
            connect[f2] = 1
        union(friend, connect, f1, f2)
        print(connect[find(friend,f1)])