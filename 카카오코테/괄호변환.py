change = {'(':')', ')':'('}

def solution(p):
    if p == '': return p

    answer = ''
    correct = False
    if p[0] == '(': correct = True # 올바른 괄호 문자열일 경우

    cnt = 0
    idx = 0
    for i, c in enumerate(p):
        if c == '(': cnt += 1
        else: cnt -= 1
        if cnt == 0: idx = i; break

    if correct: return p[:idx+1] + solution(p[idx+1:])
    
    return '(' + solution(p[idx+1:]) + ')' + ''.join(map(lambda x : change[x] ,p[1:idx]))

P = ["(()())()", ")(", "()))((()", ")()()()("]
result = ["(()())()", "()", "()(())()", "(((())))"]

for p, r in zip(P, result): print(solution(p), r)
# print(''.join(list(map(lambda x : change[x] ,result[-1]))))