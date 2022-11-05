""" 빛의 경로 사이클

중요
    - 만들어지는 빛의 경로 사이클의 모든 길이

인사이트
    - 사이클이기 때문에 중복되는 경로가 발생하면 안됨.
    - 어느지점에서 시작해도 사이클은 순회한다.

풀이
    - grid를 받고 경로를 만들 수 있어야 함.
        - node의 값에 따라서 갈 수 있는 위치가 달라진다.
    - 방향을 나타낼 수 있어야 한다.. (0, 1), (1, 0) 이런 것들
"""

# ->, ^, <-, v
import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)


def solution(grid):
    answer = []
    move = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    visited = defaultdict(bool)

    def dfs(y, x, m_idx):
        if visited[y, x, m_idx]:
            return 0
        visited[y, x, m_idx] = True
        if grid[y][x] == "L":
            m_idx += 1
        elif grid[y][x] == "R":
            m_idx -= 1
        m_idx = m_idx % len(move)
        ny, nx = y + move[m_idx][0], x + move[m_idx][1]
        return dfs(ny % len(grid), nx % len(grid[0]), m_idx) + 1

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for m_idx in range(4):
                answer.append(dfs(y, x, m_idx))

    return sorted(filter(lambda x: x, answer))


print(solution(["SL", "LR"]))
print(solution(["S"]))
print(solution(["R", "R"]))
