def solution(N, stages):
    answer = [0] * (N + 1)

    for stage in stages:
        answer[stage - 1] += 1

    user_cnt = answer[-1]
    for stage in range(len(answer) - 2, -1, -1):
        user_cnt += answer[stage]
        answer[stage] = answer[stage] / user_cnt if user_cnt else 0

    answer, _ = zip(
        *sorted(enumerate(answer[:-1]), key=lambda x: x[1], reverse=True)
    )
    return list(map(lambda x: x + 1, answer))


if __name__ == "__main__":
    t_case = []
    t_case.append([5, [2, 1, 2, 6, 2, 4, 3, 3]])  # return [3,4,2,1,5]
    t_case.append([4, [4, 4, 4, 4, 4]])  # return [4,1,2,3]

    for tc in t_case:
        print(solution(*tc))
