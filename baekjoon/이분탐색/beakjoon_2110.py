N, C = map(int, input().split())
house = [0] * N
for i in range(N): house[i] = int(input())
house.sort()

print(N, C, house)

min_val = min(house)
max_val = max(house)

# 이분 탐색을 사용하여 최대 거리 찾기
start = 1
end = (max_val-min_val)//(C-1) # 최대 거리

while(start <= end):
    mid = (start+end)//2

    count = 1
    prev_h_loc = house[0]
    for h_loc in house[1:]:
        if h_loc-prev_h_loc >= mid:
            prev_h_loc = h_loc
            count += 1

    if count < C: # 공유기 수가 작으면 (거리를 좁힌다)
        end = mid-1
    else: # 공유기 수가 같거나 크면 (거리를 늘린다)
        start = mid+1

print(end)