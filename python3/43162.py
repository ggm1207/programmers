from collections import defaultdict

def solution(n, computers):
    not_visited = {i for i in range(n)}
    visited = set()

    nexts = defaultdict(set)
    comp_len = len(computers)

    for i in range(comp_len):
        for j in range(comp_len):
            if i == j:
                continue

            if computers[i][j] == 1:
                nexts[i].add(j)

    def dfs(node):
        nonlocal not_visited, visited
        visited.add(node)
        next_nodes = nexts[node]

        for next_node in next_nodes:
            if next_node in visited:
                continue
            dfs(next_node)
            not_visited.remove(next_node)

    cnt = 0 
    while not_visited:
        node = not_visited.pop()
        dfs(node)
        cnt += 1
        
    return cnt


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
