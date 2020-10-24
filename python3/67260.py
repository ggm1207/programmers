from collections import defaultdict, deque

def solution(n, path, order):
    visited = set()
    blocks = set()

    queue = deque([0])
    b_queue = deque([])

    direction = defaultdict(list)

    for to, fr in path:
        direction[to].append(fr)
        direction[fr].append(to)

    block_dict = {k: v for k, v in order}
    block_r_dict  = defaultdict(bool, {v: True for _, v in order})

    while queue:
        cur_node = queue.popleft()
        visited.add(cur_node)

        if block_r_dict[cur_node]:
            blocks.add(cur_node)
            continue

        try:
            if block_dict[cur_node] in blocks:
                queue.append(block_dict[cur_node])

            block_r_dict[block_dict[cur_node]] = False
            del block_dict[cur_node]
        except:
            pass

        nodes = [node for node in direction[cur_node] if node not in visited]
        queue.extend(nodes)

    return False if block_dict else True

if __name__ == "__main__":
    t_case = []
    t_case.append([9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[8,5],[6,7],[4,1]]]) # return true
    t_case.append([9,[[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]],[[4,1],[5,2]]]) # return true
    t_case.append([9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[4,1],[8,7],[6,5]]]) # return false

    for tc in t_case:
        print(solution(*tc))
