def is_prime_num(num):
    if num == 1: return False
    for i in range(2, num):
        if i*i > num: break
        if num%i==0: return False
    return True

def solution(n, k):
    answer = 0
    new_num = ''

    while n>=k:
        new_num = str(n%k) + new_num
        n //= k
    new_num = str(n%k) + new_num
    
    print(new_num)
    print(new_num.split('0'))

    for num in new_num.split('0'):
        if len(num) > 0 and is_prime_num(int(num)): answer+=1
    return answer


print(solution(11, 2))
print(solution(437674, 3))
print(solution(110011, 10))

print(is_prime_num(2))

print(is_prime_num(3))

print(is_prime_num(4))

print(is_prime_num(11))