def solution(brown, yellow):
    answer = []

    num_add = (brown-4)//2
    num_mul = yellow

    for i in range(1,num_mul+1):
        if i*i > num_mul: break
        if num_mul%i == 0 and (num_mul//i) + i == num_add:
            return [num_mul//i+2, i+2]


    return answer

print(solution(10,2)) # 4,3
print(solution(8,1)) # 3,3
print(solution(24,24)) # 8,6