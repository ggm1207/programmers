from collections import defaultdict


def get_block_pos_dict(board, N):
    block_pos_dict = defaultdict(list)
    for y in range(N):
        for x in range(N):
            if board[y][x] != 0:
                block_pos_dict[board[y][x]].append((y, x))

    return block_pos_dict


def get_min_max_yx(block_pos):
    min_yx, max_yx = [100, 100], [0, 0]
    for y, x in block_pos:
        min_yx[0], min_yx[1] = min(min_yx[0], y), min(min_yx[1], x)
        max_yx[0], max_yx[1] = max(max_yx[0], y), max(max_yx[1], x)
    return min_yx, max_yx


def get_black_block_list(board, min_yx, max_yx, block_num):
    black_list = []
    # print(min_yx, max_yx)
    for y in range(min_yx[0], max_yx[0] + 1):
        for x in range(min_yx[1], max_yx[1] + 1):
            # print(y, x, end = ' ')
            if board[y][x] != block_num:
                black_list.append((y, x))
    return black_list


def is_black_possible(board, y, x):
    while y > -1:
        if board[y][x] == 0:
            y -= 1
            continue
        return False
    return True


def delete_block(board, block_pos):
    for y, x in block_pos:
        board[y][x] = 0


def solution(board):
    answer = 0
    N = len(board)
    deleted = set()
    block_pos_dict = get_block_pos_dict(board, N)
    # main
    while True:
        delete_cnt = 0

        for block_num, block_pos in block_pos_dict.items():
            if block_num in deleted:
                continue

            min_yx, max_yx = get_min_max_yx(block_pos)
            black_list = get_black_block_list(board, min_yx, max_yx, block_num)
            flag = all([is_black_possible(board, y, x) for y, x in black_list])

            if flag:
                delete_block(board, block_pos)
                deleted.add(block_num)
                delete_cnt += 1

        if delete_cnt:
            answer += delete_cnt
            continue

        break

    return answer


if __name__ == "__main__":
    t_case = []
    t_case.append(
        [
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
                [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
                [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
                [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
                [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
                [1, 1, 1, 0, 0, 0, 0, 0, 0, 5],
            ],
        ]
    )  # return 2
    t_case.append(
        [
            [
                [6, 6, 6, 7, 7, 7, 8, 8, 8, 0],
                [0, 6, 0, 0, 7, 0, 8, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
                [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
                [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
                [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
                [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
                [1, 1, 1, 0, 0, 0, 0, 0, 0, 5],
            ],
        ]
    )  # return 0
    t_case.append(
        [
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
                [0, 2, 3, 0, 0, 0, 0, 0, 0, 0],
                [1, 2, 3, 3, 0, 0, 0, 0, 0, 0],
                [1, 2, 2, 4, 0, 0, 0, 0, 0, 0],
                [1, 1, 4, 4, 4, 0, 0, 0, 0, 0],
            ],
        ]
    )  # return 6
    for tc in t_case:
        print(solution(*tc))
