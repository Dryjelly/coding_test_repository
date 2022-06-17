import sys
input = sys.stdin.readline

n = int(input())
check = [0 for _ in range(n+1)]
for _ in range(n):
    numbers = list(map(int,input().split()))
    for i in range(len(numbers)-1,-1,-1):
        if i == 0:
            check[i] = numbers[i] + check[i]
        else:
            check[i] = numbers[i] + max(check[i-1], check[i])
    print(check)
print(max(check))