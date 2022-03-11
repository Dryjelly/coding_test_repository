# class Node(object):
#     def __init__(self, loc, data):
#         self.loc = loc
#         self.data = data
#         self.left = self.right = None

# class BinarySearchTree(object):
#     def __init__(self):
#         self.root = None

#     def insert(self, loc, data):
#         self.root = self._insert_value(self.root, loc, data)
#         return self.root is not None

#     def _insert_value(self, node, loc, data):
#         if node is None:
#             node = Node(loc, data)
#         else:
#             if loc[0] <= node.loc[0]:
#                 node.left = self._insert_value(node.left, loc, data)
#             else:
#                 node.right = self._insert_value(node.right, loc, data)
#         return node

#     def pre_order(self):
#         answer = []
#         def _pre_order(node):
#             if node is None: pass
#             else:
#                 answer.append(node.data)
#                 _pre_order(node.left)
#                 _pre_order(node.right)
#         _pre_order(self.root)
#         return answer

#     def post_order(self):
#         answer = []
#         def _post_order(node):
#             if node is None: pass
#             else:
#                 _post_order(node.left)
#                 _post_order(node.right)
#                 answer.append(node.data)
#         _post_order(self.root)
#         return answer

# def solution(nodeinfo):
#     index = sorted(range(1,len(nodeinfo)+1), key=lambda x:nodeinfo[x-1][-1], reverse = True)
#     # nodeinfo.sort(key=lambda x:x[-1], reverse = True)
#     # print(nodeinfo)
#     print(index)
#     bst = BinarySearchTree()
#     for i in index: bst.insert(nodeinfo[i-1],i)
#     print(bst.pre_order())
#     print(bst.post_order())
#     answer = [bst.pre_order(),bst.post_order()]
#     return answer

# print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
# # print(solution([[2,2]]))


# def solution(n, times):
#     answer = 0
#     return answer



# def solution(n):
#     board = [0 for _ in range(n)]
#     board[0] = 1
#     board[1] = 2

#     for i in range(2,n):
#         board[i] = (board[i-1] + board[i-2])%1000000007

#     print(board)
#     return board[n-1]

# print(solution(4))



def solution(n, computers):
    visited = [0 for _ in range(n)]

    def dfs(node):
        visited[node] = 1
        for next_node in range(n):
            if node == next_node: continue
            if computers[node][next_node] and visited[next_node] == 0:
                dfs(next_node)

    cnt = 0
    for i in range(n):
        if visited[i] == 0:
            cnt += 1
            dfs(i)
        
    return cnt

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))