import sys
input = sys.stdin.readline

A = int(input())
A_i = [0]
number = map(int, input().split())


for num in number:
    start = 1
    end = len(A_i)-1
    while(start <= end):
        mid = (start+end)//2
        if A_i[mid] < num: # 현재 값이 중간값 보다 크다면... 올라가야
            start = mid+1 
        else: # 현재 값이 중간값과 같거나 작다면... 내려가야
            end = mid-1

    if len(A_i)-1 < start:
        A_i.append(num)
    else:
        A_i[start] = num

print(A_i)
print(len(A_i)-1)

