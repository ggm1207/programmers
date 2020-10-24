from collections import defaultdict


def solution(arrows):
    answer = 0
    visited = defaultdict(int)
    cy, cx = 0, 0
    move = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]
    visited[cy, cx] += 1

    for arrow in arrows:
        y, x = move[arrow]
        cy, cx = cy + y, cx + x
        visited[cy, cx] += 1
    print(visited)
    for v in visited.values():
        if v > 1:
            answer += v - 1

    return answer


if __name__ == "__main__":
    t_case = []
    t_case.append(
        [[6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]]
    )  # return 3
    t_case.append([[6, 5, 2, 7, 1, 4, 2, 4, 6]])  # return 3
    t_case.append([[5, 2, 7, 1, 6, 3]])  # return 3
    t_case.append([[6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]])  # return 3

    for tc in t_case:
        print(solution(*tc))
