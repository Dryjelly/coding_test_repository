from collections import deque

class Node(object):
    def __init__(self, data, idx):
        self.data = data
        self.idx = idx
        self.child = []

class BinarySearchTree(object):
    def __init__(self, info):
        self.nodes = [Node(i,idx) for idx,i in enumerate(info)]
        self.root = self.nodes[0]

    def connect(self, edge):
        s,e = edge
        self.nodes[s].child.append(self.nodes[e])

    def pre_order(self):
        answer = []
        def _pre_order(node):
            if node is None: pass
            else:
                answer.append(node.idx)
                for next in node.child:
                    _pre_order(next)
        _pre_order(self.root)
        return answer

    def collect(self):
        sheep = 0
        wolf = 0
        will_visit = deque([(self.root, sheep, wolf)])

        def _collect(node, sheep, wolf):
            if node.data == 0: # 양 만나면 계속 탐색
                for next in node.child: _collect(next, sheep+1, wolf)
            else: # 늑대 만나면 다음 node 넣고 멈춤
                for next in node.child: will_visit.append((next, sheep, wolf+1)) # 저장
                return
        
        while will_visit:
            temp_len = len(will_visit)
            for _ in range(temp_len):
                next, cur_sheep, cur_wolf = will_visit.popleft()
                _collect(next)
            wolf += 1
            if sheep <= wolf : break

        return sheep


def solution(info, edges):
    answer = 0
    bst = BinarySearchTree(info)
    for e in edges: bst.connect(e)
    answer = bst.collect()
    # print(bst.pre_order())


    return answer


print(solution([0,0,1,1,1,0,1,0,1,0,1,1],
[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))

print(solution([0,1,0,1,1,0,1,0,0,1,0],
[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))