def solution(numbers):
    answer = 0

    def prime_number(numbers):
        answer = 0
        def permutation(num_list, r, index):
            for i in range(len(num_list)):
                if index==0 and num_list[i] == '0': continue
                if r == 1: yield num_list[i]
                else:
                    for next in permutation(num_list[:i]+num_list[i+1:], r-1, index+1):
                        yield num_list[i]+next

        for i in range(len(numbers)):
            for number in map(int,set(permutation(numbers,i+1,0))):
                if is_prime(number): answer += 1
        return answer

    def is_prime(num):
        if num == 1: return False
        for i in range(2,num):
            if i*i > num: break
            if num%i == 0: return False
        return True
    
    answer = prime_number(numbers)
    return answer

# print(solution("17")) # 3
print(solution("011")) # 2