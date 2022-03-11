from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for depart, dest in tickets:
        graph[depart]
    print(graph)

    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])) #["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])) #["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]