def solution(triangle):
    answer = 0

    triangle_sum = [t[:] for t in triangle]
    triangle_sum[1][0] += triangle_sum[0][0]
    triangle_sum[1][1] += triangle_sum[0][0]

    print(triangle_sum)

    for i in range(2, len(triangle)):
        for j in range(i+1):
            if j == 0: triangle_sum[i][j] += triangle_sum[i-1][j]
            elif j == i: triangle_sum[i][j] += triangle_sum[i-1][j-1]
            else:
                triangle_sum[i][j] += max(triangle_sum[i-1][j-1], triangle_sum[i-1][j])

    print(triangle_sum)
    answer = max(triangle_sum[-1])
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
result = 30
print(solution(triangle), result)