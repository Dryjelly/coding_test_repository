N, M = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)

while(start <= end):
    mid = (start+end)//2
    length = 0
    for t in tree:
        length += max(0, t-mid)

    if length < M : end = mid-1 # 잘린 길이가 짧음
    else: start = mid+1 # 잘린 길이가 길거나 같음

print(end)