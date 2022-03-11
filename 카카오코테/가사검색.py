import sys
sys.setrecursionlimit(100001)

def solution(words, queries):
    answer = []
    class Node:
        def __init__(self, key, data=None):
            self.key = key
            self.data = data
            self.next = {}
            self.length = {}

    class Trie:
        def __init__(self):
            self.head = Node(None)

        def insert(self, string):
            cur_node = self.head
            for c in string:
                if len(string) not in cur_node.length:
                    cur_node.length[len(string)] = 1
                else: cur_node.length[len(string)] += 1
                if c not in cur_node.next:
                    cur_node.next[c] = Node(c)
                cur_node = cur_node.next[c]
            cur_node.data = string

        def show_all(self, node):
            if node.data == None: print(node.key, end=' '); print(node.length, end=' ')
            else : print(node.key , node.data)
            for next in node.next.values(): self.show_all(next)
            
        def search(self, string):
            cur_node = self.head
            for c in string:
                if c in cur_node.next: cur_node = cur_node.next[c]
                else: return False
                if c == '?':
                    pass # next node 다 넣기
                
            return 0

        def counter(self, node, string, idx):
            if len(string) == idx: # 찾는 문자열 끝 도달
                if node.data != None: print(node.data); return 1 # 단어가 존재함
                else: return 0 # 단어가 없음
            c = string[idx]
            if c == '?': # 현재 문자가 wildcard 일 때
                cnt = 0
                for next in node.next.values(): # 다음 모든 노드 탐색
                    cnt += self.counter(next, string, idx+1)
                return cnt
            if c in node.next: return self.counter(node.next[c], string, idx+1) # 다음 노드에서 문자를 찾음
            return 0 # 다음 노드에 문자가 없음

        def counter_v2(self, node, string, idx):
            c = string[idx] # 다음 노드에서 찾을 문자
            if c == '?': # 문자가 wildcard 일 때
                if len(string) not in node.length: return 0
                return node.length[len(string)]
            if c in node.next: return self.counter_v2(node.next[c], string, idx+1) # 다음 노드에서 문자를 찾음
            return 0 # 다음 노드에 문자가 없음

    pre_trie = Trie()
    post_trie = Trie()
    for w in words:
        pre_trie.insert(w)
        post_trie.insert(w[::-1])
    pre_trie.show_all(pre_trie.head)
    # trie.show_all(trie.head)
    # for q in queries :print(trie.counter(trie.head, q, 0))
    for q in queries: 
        if q[0] != '?':
            answer.append(pre_trie.counter_v2(pre_trie.head, q, 0))
        else:
            answer.append(post_trie.counter_v2(post_trie.head, q[::-1], 0))
    
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

result = [3, 2, 4, 1, 0]

print(solution(words, queries))