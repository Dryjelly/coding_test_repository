from collections import defaultdict

def solution(clothes):
    answer = 1

    clothes_dict= defaultdict(int)
    for value, key in clothes: clothes_dict[key] += 1

    for value in clothes_dict.values(): 
        answer *= value+1 

    return answer-1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([["smoky_makeup", "face"]]))