def max_lan_line(length, lan_lines):
    count = 0
    for lan in lan_lines:
        count += lan//length
    return count

lan_lines = []

K, N = map(int, input().split())

for _ in range(K): lan_lines.append(int(input()))

# lan_lines.sort()
# print(K, N, lan_lines)

# count = 0
# max_value = lan_lines[-1]
# min_value = lan_lines[0]

# print(max_lan_line(min_value, lan_lines))

start = 1
end = max(lan_lines)

while start <= end:
    mid = (start+end)//2
    count = max_lan_line(mid, lan_lines)

    if count >= N: # 랜선이 많거나 같음
        start = mid+1
    elif count < N: # 랜선이 모자람
        end = mid-1
print(end)