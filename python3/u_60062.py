from itertools import combinations, permutations

test_case = 0


def solution(n, weak, dist):
    global test_case
    dist.sort(reverse=True)
    weak_bit = {weak[idx]: pow(2, idx) for idx in range(len(weak))}
    weak_len = len(weak)
    test_case += 1
    weak_set = set(weak)
    answer = pow(2, len(weak)) - 1

    weak_dict = {wk: dict() for wk in weak}

    def get_covered_weak_pos(weak_pos, dist):
        bit = weak_bit[weak_pos]
        for cur_pos in range(weak_pos, weak_pos + dist + 1):
            cur_pos = cur_pos % n
            if cur_pos in weak_set:
                bit = bit | weak_bit[cur_pos]

        return bit

    for d in dist:
        for weak_pos, weak_dictionary in weak_dict.items():
            weak_dict[weak_pos][d] = get_covered_weak_pos(weak_pos, d)

    for peopel_num in range(1, len(dist) + 1):
        for weak_pos in permutations(weak, peopel_num):
            cover_bit = 0

            for idx, wp in enumerate(weak_pos):
                cover_bit = cover_bit | weak_dict[wp][dist[idx]]

            if cover_bit == answer:
                return peopel_num

    return -1


if __name__ == "__main__":
    t_case = []
    t_case.append([12, [1, 5, 6, 10], [1, 2, 3, 4]])  # return 2
    t_case.append([12, [1, 3, 4, 9, 10], [3, 5, 7]])  # return 1
    t_case.append(
        [
            200,
            [1, 3, 4, 9, 10, 15, 40, 80, 90, 100, 120, 150, 170, 180, 190],
            [3, 5, 7, 9, 11, 13, 15, 16],
        ]
    )  # return -1

    for tc in t_case:
        print(solution(*tc))
