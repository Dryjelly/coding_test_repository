import sys
sys.setrecursionlimit(10 ** 6)

def solution(k, num, links):
    answer = 0

    p = [i for i in range(len(num))]
    p_sum = num[:]

    def find(node):
        if p[node] == node: return node
        return find(p[node])

    def go_up_sum(node, sum_num):
        p_sum[node] += sum_num
        if p[node] == node: return node
        return go_up_sum(p[node], sum_num)

    def union(p_node):
        c_nodes = links[p_node]
        sum_num = 0
        for c_node in c_nodes:
            if c_node == -1: continue
            p[c_node] = p_node
            sum_num += p_sum[c_node]
        go_up_sum(p_node, sum_num)

    for p_node in range(len(links)):
        union(p_node)

    root_node = find(0)
    right = p_sum[root_node]
    left = max(max(num), right//k)
    
    # print('root_node =', root_node)
    # print('p = ',p)
    # print('p_sum = ',p_sum)

    def check(root, L):

        def dfs(node):
            if p_sum[node] <= L: return (1, p_sum[node])

            child = []
            for c_node in links[node]:
                if c_node == -1:
                    child.append((1,0))
                else:
                    child.append(dfs(c_node))

            # 1. 모든 자식을 현재 노드와 합쳐도 L 초과하지 않음
            if num[node] + child[0][1] + child[1][1] <= L:
                return (child[0][0] + child[1][0] - 1, num[node] + child[0][1] + child[1][1])
            # 2. 두 자식 중 하나의 자식만 선택 가능함
            if num[node] + child[0][1] <= L or num[node] + child[1][1] <= L:
                return (child[0][0] + child[1][0], num[node] + min(child[0][1], child[1][1]))
            # 3. 모두 선택 안함
            if num[node] <= L:
                return (child[0][0] + child[1][0] + 1, num[node])

        group, _ = dfs(root)
        if group <= k: return True
        return False
    
    mid = -1
    # 이분 탐색
    while(left <= right):
        mid = (left+right)//2
        # 가능하다면 mid 줄이기
        if check(root_node, mid):
            right = mid-1
        # 불가능하다면 mid 늘이기
        else:
            left = mid+1

    answer = left

    return answer


print(solution(3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1], [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))
# 40
print(solution(1, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
# 27
print(solution(2, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
# 14
print(solution(4, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
# 9
print(solution(1, [100], [[-1, -1]]))