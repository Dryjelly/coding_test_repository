def solution(s):
    answer = 1
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n): dp[i][i] = 1

    # print(dp)

    for i in range(n-1):
        if s[i] == s[i+1]: dp[i][i+1] = 1 ; answer = 2

    length = 2
    while length < n:
        for i in range(n-length):
            if dp[i+1][i+length-1] == 1 and s[i] == s[i+length]: dp[i][i+length] = 1 ; answer = length+1
        length += 1


    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    return answer

print(solution("abcdcba"))
print(solution("abacde"))
print(solution("aa"))