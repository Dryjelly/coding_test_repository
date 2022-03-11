import bisect
from itertools import permutations

def solution(n, weak, dist):
    selected_dist = []

    def check(new_weak, selected_dist):
        start_point = new_weak[0]
        idx = 0
        for d in selected_dist:
            start_point += d
            idx += bisect.bisect_right(new_weak[idx:], start_point)
            if idx == len(new_weak): return True
            start_point = new_weak[idx]
        return True if idx == len(new_weak) else False

    for d_i in range(len(dist)):
        selected_dist.append(dist[len(dist)-1-d_i])
        for w_i in range(len(weak)):
            new_weak = weak[w_i:] + [w+n for w in weak[:w_i]]
            for p_dist in permutations(selected_dist):
                if check(new_weak, p_dist): return d_i+1

    return -1

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

# print(bisect.bisect_right(weak, 10))
# print(list(permutations([1,2,3])))

print('result = 2\n', solution(n,weak,dist))

n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]

print('result = 1\n', solution(n,weak,dist))