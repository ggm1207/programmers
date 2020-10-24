def solution(brown, yellow):
    flag = False
    for x in range(1, 5000):
        for y in range(1, 5000):
            if (x + y - 2) * 2 == brown and (x - 2) * (y - 2) == yellow:
                answer = [y, x]
                flag = True
                break
        if flag:
            break
    return answer


if __name__ == "__main__":
    t_case = []
    t_case.append([10, 2])
    t_case.append([8, 1])
    t_case.append([24, 24])

    for tc in t_case:
        print(solution(*tc))

