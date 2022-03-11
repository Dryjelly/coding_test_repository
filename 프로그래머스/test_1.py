
# def solution(strings, n):
#     answer = []

#     def quick_sort(arr):
#         if len(arr) <= 1:
#             return arr
#         pivot = arr[len(arr) // 2][n]
#         lesser_arr, equal_arr, greater_arr = [], [], []
#         for num in arr:
#             if num[n] < pivot:
#                 lesser_arr.append(num)
#             elif num[n] > pivot:
#                 greater_arr.append(num)
#             else:
#                 equal_arr.append(num)
#         return quick_sort(lesser_arr) + sorted(equal_arr) + quick_sort(greater_arr)

#     answer = quick_sort(strings)

#     return answer

# print(solution(["sun", "bed", "car"],1))
# print(solution(["abce", "abcd", "cdx"],2))

def solution(arr):
    if len(arr) == 1 : return [-1]
    answer = arr
    answer.remove(min(answer))
    return answer

print(solution([4,3,2,1]))
print(solution([10]))