def solution(begin, end):
    answer = []

    for block in range(begin, end + 1):
        flag = True
        for t in range(2, int(block ** 0.5 + 1.5)):
            if not (block % t):
                answer.append(block // t)
                flag = False
                break
        if not flag:
            continue

        if block == 1:
            answer.append(0)
        else:
            answer.append(1)

    return answer


if __name__ == "__main__":
    t_case = []
    t_case.append([1, 10])  # return [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]
    t_case.append([23, 39])
    t_case.append([999999999, 1000000000])

    for tc in t_case:
        print(solution(*tc))
