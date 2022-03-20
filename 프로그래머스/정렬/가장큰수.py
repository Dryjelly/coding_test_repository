def solution(numbers):
    answer = ''

    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x:x*3, reverse=True)
    print(numbers)
    answer = str(int(''.join(numbers)))
    return answer

print(solution([6, 10, 2])) # "6210"
print(solution([3, 30, 34, 5, 9])) # "9534330"
print(solution([3, 30, 34, 5, 9, 301, 340, 31, 310, 304, 3429, 349, 342, 3421]))