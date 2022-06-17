def solution(number, k):
    remove = k
    answer = [number[0]]
    
    for n in number[1:]:
        while(answer and k>0):
            if answer[-1] < n:
                k -= 1
                answer.pop()
            else: break
        answer.append(n)
        
    if len(number)-remove != len(answer): answer = answer[:-k]
    return "".join(answer)

print(solution("1924",2), "94")
print(solution("1231234",3), "3234")
print(solution("4177252841",4), "775841")

print(solution("654321",1), "65432")
print(solution("654321",5), "6")