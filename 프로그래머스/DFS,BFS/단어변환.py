from collections import deque

def word_check(word_1, word_2):
    diff = 0
    for w_1, w_2 in zip(word_1, word_2):
        if w_1 != w_2: diff += 1
    if diff == 1: return 1
    else: return 0

def solution(begin, target, words):
    answer = 0
    visited = [False for _ in range(len(words))]
    q = deque([begin])
    while q:
        q_size = len(q)
        for q_s in range(q_size):
            word = deque.popleft(q)
            for i in range(len(words)):
                if not visited[i] and word_check(word, words[i]):
                    if words[i] == target: return answer+1
                    visited[i] = True
                    deque.append(q, words[i])
        answer += 1
    
    return 0

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])) #4
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"])) #0
