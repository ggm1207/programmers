import heapq
from collections import defaultdict

def solution(board):
    N = len(board)
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = defaultdict(int)
    queue = []

    for y, x in [(1, 0), (0, 1)]:
        if board[y][x] == 1:
            continue
        i = move.index((y, x))
        queue.append((100, y, x, i))
        visited[y, x] = 100

    heapq.heapify(queue)

    while queue:
        cost, y, x, r = heapq.heappop(queue)

        if (y, x) == (N-1, N-1):
            return cost

        for i, m in enumerate(move):
            ny, nx = y + m[0], x + m[1]

            if sorted([i, r]) in [[0, 1], [2, 3]]:  # back case
                continue

            if not (0 <= ny < N and 0 <= nx < N):  # range case
                continue

            if board[ny][nx] == 1:  # wall case
                continue

            n_cost = cost + 100 if i == r else cost + 600

            if visited[ny, nx] != 0 and visited[ny, nx] < n_cost - 400:
                continue

            heapq.heappush(queue, (n_cost, ny, nx, i))
            visited[ny, nx] = n_cost

    return cost

if __name__ == "__main__":
    t_case = []
    t_case.append([[[0,0,0],[0,0,0],[0,0,0]]]) # return 900
    t_case.append([[[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]]) # return 3800
    t_case.append([[[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]]) # return 2100
    t_case.append([[[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]]) # return 3200

    for tc in t_case:
        print(solution(*tc))
