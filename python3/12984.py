from collections import defaultdict


def solution(land, P, Q):
    block_counter = defaultdict(int)
    block_total_num = 0
    cur_floor_block_num = 0

    N = len(land)
    linear_land = sum(land, [])

    for block in linear_land:
        block_counter[block] += 1
        block_total_num += block

    costs = []
    cur_floor_block_num = N ** 2
    block_add_total_num = 0
    prev_floor = 0

    for floor, block_num in sorted(block_counter.items(), key=lambda x: x[0]):
        block_add_total_num += (floor - prev_floor) * cur_floor_block_num
        cur_floor_block_num -= block_num
        cost = ((N * N * floor) - block_add_total_num) * P + (
            block_total_num - block_add_total_num
        ) * Q
        prev_floor = floor
        costs.append(cost)

    return min(costs)


if __name__ == "__main__":
    t_case = []
    t_case.append([[[1, 2], [2, 3]], 3, 2])  # return 5
    t_case.append([[[4, 4, 3], [3, 2, 2], [2, 1, 0]], 5, 3])  # return 33

    for tc in t_case:
        print(solution(*tc))
