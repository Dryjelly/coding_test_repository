def solution(s):
    answer = ''

    number = {
        'zero':'0',
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }

    temp = ''
    for t_s in s:
        if t_s>='0' and t_s<='9':
            answer += t_s
            temp = ''
        else:
            temp += t_s
            if temp in number:
                answer += number[temp]
                temp = ''
    answer += temp

    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))