import sys

input = sys.stdin.readline

N = int(input())
s,g,p,d = map(int, input().split())
mvp = list(input().rstrip())

money = {'B':s-1, 'S':g-1, 'G':p-1, 'P':d-1}

temp = 0
total_money = 0
for m in mvp:
    if m == 'D': total_money += d; continue
    temp = money[m]-temp
    total_money += temp
print(total_money)