def solution(food_times, k):
    cycle_len = len(food_times)
    food_times = sorted(enumerate(food_times), key=lambda x: x[1], reverse=True)
    prev_food_time = 0

    while True:
        food_idx, food_time = food_times.pop()
        next_cylce_cnt = (food_time - prev_food_time) * cycle_len

        if k < next_cylce_cnt:
            food_times.append((food_idx, food_time))
            break

        if not food_times:
            return -1

        # same food cnt
        while food_times[-1][1] == food_time:
            cycle_len -= 1
            food_times.pop()

            if not food_times:
                return -1

        # parameter update
        k, prev_food_time = k - next_cylce_cnt, food_time
        cycle_len -= 1

    food_times = sorted(food_times)

    return food_times[k % cycle_len][0] + 1 if food_times else -1


if __name__ == "__main__":
    t_case = []
    # t_case.append([[3, 1, 2], 5])  # return 1
    # t_case.append([[1, 1, 1, 1, 1, 1, 1, 1], 5])  # return 6
    # t_case.append([[1, 1, 1, 1, 1, 1, 1, 1], 9])  # return -1
    # t_case.append([[1, 2, 3, 4, 5, 6, 7, 8], 9])  # return 2
    # t_case.append([[8, 7, 6, 5, 4, 3, 2, 1], 9])  # return 2
    t_case.append([[8, 7, 6, 5, 4, 3, 2, 1], 60])  # return -1
    t_case.append([[8, 7, 6, 5, 4, 3, 2, 1], 36])  # return 1
    t_case.append([[1], 1])  # return 1

    for tc in t_case:
        print(solution(*tc))
