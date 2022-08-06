from collections import defaultdict


def solution(grid):
    answer = []
    visited = defaultdict(bool)

    direction = []
    height, width = len(grid), len(grid[0])

    left = lambda pos: (pos[0], (pos[1] - 1) % width)
    right = lambda pos: (pos[0], (pos[1] + 1) % width)
    up = lambda pos: ((pos[0] - 1) % height, pos[1])
    down = lambda pos: ((pos[0] + 1) % height, pos[1])

    moves = {"l": left, "r": right, "u": up, "d": down}
    move = lambda node: moves[d] if node[0] == "s"

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            direction.append([y, x, "l"])
            direction.append([y, x, "r"])
            direction.append([y, x, "u"])
            direction.append([y, x, "d"])

    def dfs(y, x, d):
        nonlocal answer

        for my, mx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = my + y, mx + x

            if visited[y, ny, x, nx]:
                answer.append(cycle)
                continue

            visited[y, ny, x, nx] = True
            dfs(ny, nx, cycle)

    for y, x, d in direction:
        if visited[y, x, d]:
            continue

        dfs(y, x, d)

    return answer
