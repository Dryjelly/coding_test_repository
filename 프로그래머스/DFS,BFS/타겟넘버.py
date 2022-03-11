def solution(numbers, target):
    global answer
    answer=0

    def dfs(idx, num):
        global answer
        if idx == len(numbers):
            # print(num)
            if target == num:
                # print(num)
                answer+=1
            return
        dfs(idx+1, num+numbers[idx])
        dfs(idx+1, num-numbers[idx])

    dfs(0, 0)

    return answer

print(solution([1, 1, 1, 1, 1],3)) #5
print(solution([4, 1, 2, 1], 4))  #2