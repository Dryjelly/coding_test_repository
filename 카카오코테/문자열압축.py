# def solution(s):
#     shortest = len(s)

#     for i in range(1, len(s)//2+1):
#         # print(f'i = {i}')
#         count = 0
#         num_cnt = 0
#         prev = s[:i]
#         p_i = i
#         q = len(s)//i - 1
#         while q:
#             # 같은 문자열
#             if prev == s[p_i:p_i+i]: 
#                 count += i 
#                 num_cnt += 1
#             # 다른 문자열, 기록 중
#             elif num_cnt != 0:
#                 # print(f'num_cnt = {num_cnt}')
#                 count -= len(str(num_cnt+1))
#                 num_cnt = 0
#             prev = s[p_i:p_i+i]
#             p_i += i
#             q -= 1
#         if num_cnt != 0: count -= len(str(num_cnt+1))
#         # print(f'count = {len(s)-count}')
#         if len(s)-count < shortest: shortest = len(s)-count

#     return shortest

def solution(s):
    sortest = len(s)
    for cut in range(1, len(s)//2 + 1):
        prev = s[:cut]
        start = cut
        temp_cnt = 0
        temp_s = ""
        while start + cut <= len(s): # 자르는게 길이 초과하지 않을 때
            cur = s[start:start+cut]
            if prev == cur: # 같은 경우
                temp_cnt += 1
            else: # 다른 경우
                if temp_cnt == 0: # 누적된게 없음
                    temp_s += prev
                else: # 누적된게 있음
                    temp_s += str(temp_cnt+1)
                    temp_s += prev
                prev = cur
                temp_cnt = 0

            start += cut
        
        if temp_cnt: temp_s += str(temp_cnt+1) + prev
        else: temp_s += prev

        temp_s += s[start:start+cut]
        # print(temp_s, cut)
        if len(temp_s) < sortest: sortest = len(temp_s)


    return sortest

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("acacacbacacac"))
print(solution("acacacacacacbacacacacacac"))
print(solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))