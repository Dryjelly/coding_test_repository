N = int(input())
k = int(input())

def check(num):
    cnt = 0
    for i in range(1, N+1):
        cnt += min(num//i,N)
 
    return cnt

# 이분 탐색을 사용
start = 1
end = k

while(start <= end):
    mid = (start+end)//2
    cnt = check(mid)

    if cnt < k: # 값이 작으면
        start = mid + 1
    else:
        end = mid - 1

print(start)