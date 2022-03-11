def has_child(tree, node):
    if len(tree[node]) == 0: return False
    return True

def min_cost_select(tree, sales, node):

    child_cost_sub = []
    # 현재 node 포함 되었을 경우
    cur_node_in_cost = sales[node-1]
    for c in tree[node]: # 자식들 확인
        c_n_i, c_n_o = min_cost_select(tree, sales, c)
        child_cost_sub.append(c_n_i - c_n_o)
        if has_child(tree, c): cur_node_in_cost += min(c_n_i, c_n_o)

    # 현재 node 포함 안 되었을 경우
    cur_node_out_cost = cur_node_in_cost - sales[node-1]
    if has_child(tree, node):
        min_value = min(child_cost_sub)
        if min_value > 0: cur_node_out_cost += min_value

    return [cur_node_in_cost, cur_node_out_cost]

def solution(sales, links):

    tree = [[] for _ in range(len(sales)+1)]
    for p, c in links:
        tree[p].append(c)
    print(tree)

    print(min_cost_select(tree, sales, 1))

    answer = min(min_cost_select(tree, sales, 1))
    return answer

sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
result = 44

print(f"solution = {solution(sales, links)}, result = {result}")
