def solution(n):
    answer = ''
    # n += n//4
    while(n):
        print('div', n, n%3)
        ad = n%3
        n //= 3
        if ad == 0:
            answer = '4' + answer
            n -= 1
        else:
            answer = str(ad) + answer
        
    return answer

for i in range(11):
    print(i, solution(i))