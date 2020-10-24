import heapq
from collections import defaultdict

def solution(m, n, puddles):
    queue = []
    heapq.heapify(queue)
    heapq.heappush(queue, (0, 0, 0, 1))

    maps_cnt = defaultdict(int)
    paths = defaultdict(int)
    visited = defaultdict(bool)
    paths[0, 0] = 1
    maps_cnt[0, 0] = 1
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    maps = [[0 for _ in range(m)] for _ in range(n)]

    def check(y, x):
        return ( 0 <= y < n and 0 <= x < m and [x + 1, y + 1] not in puddles)

    def insert(y, x, cnt, path):
        if not check(y, x):
            return 
        # 여기서 path 값을 내가 온 path 값
        if maps_cnt[y, x] == 0: # 최단경로로 처음 도달한 경우
            maps_cnt[y, x] = cnt % 1000000007
            paths[y, x] += path % 1000000007
        elif maps_cnt[y, x] == cnt: # 다른 최단경로
            paths[y, x] += path
        else:
            return
        if not visited[cnt, y, x]:
            visited[cnt, y, x] = True
            heapq.heappush(queue, (cnt, y, x, paths[y, x] % 1000000007))

    while queue:
        cnt, y, x, path = heapq.heappop(queue)

        for my, mx in moves:
            insert(y+my, x+mx, cnt + 1, paths[y, x])
        
    return paths[n-1, m-1] % 1000000007

if __name__ == "__main__":
    t_case = []
    t_case.append([4, 3, [[2, 2]]])
    t_case.append([4, 3, [[2, 2], [2, 3], [3, 2]]])
    t_case.append([5, 4, [[2, 1], [2, 2], [2, 3], [4, 4], [4, 3], [4, 2]]])
    t_case.append([4, 3, [[]]])
    t_case.append([100, 100, [[]]])
    t_case.append([5, 4, [[2, 2], [2, 3], [4, 2], [4, 3], [4, 4]]])

    for tc in t_case:
        print(solution(*tc))
