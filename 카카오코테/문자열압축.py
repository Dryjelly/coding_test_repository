def solution(s):
    shortest = len(s)

    for i in range(1, len(s)//2+1):
        # print(f'i = {i}')
        count = 0
        num_cnt = 0
        prev = s[:i]
        p_i = i
        q = len(s)//i - 1
        while q:
            # 같은 문자열
            if prev == s[p_i:p_i+i]: 
                count += i 
                num_cnt += 1
            # 다른 문자열, 기록 중
            elif num_cnt != 0:
                # print(f'num_cnt = {num_cnt}')
                count -= len(str(num_cnt+1))
                num_cnt = 0
            prev = s[p_i:p_i+i]
            p_i += i
            q -= 1
        if num_cnt != 0: count -= len(str(num_cnt+1))
        # print(f'count = {len(s)-count}')
        if len(s)-count < shortest: shortest = len(s)-count

    return shortest

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("acacacbacacac"))
print(solution("acacacacacacbacacacacacac"))
print(solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))