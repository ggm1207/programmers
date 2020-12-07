# 1. 임의의 인전합 두 풍선을 고른 뒤, 두 풍선 중 하나를 터트립니다.
# 2. 풍선 밀착


def solution(a):
    answer = 0

    if len(a) < 3:
        return len(a)

    is_min = [[0, 0] for _ in range(len(a))]  # (l_min, r_min)
    l_min = a[0]
    r_min = a[-1]

    for i in range(1, len(a) - 1):
        l_idx = i - 1
        r_idx = len(a) - (i)

        l_min = min(l_min, a[l_idx])
        r_min = min(r_min, a[r_idx])

        is_min[i][0] = l_min
        is_min[r_idx - 1][1] = r_min

    for i in range(1, len(a) - 1):
        if is_min[i][0] < a[i] and is_min[i][1] < a[i]:
            answer += 1

    return len(a) - answer


if __name__ == "__main__":
    t_case = []
    t_case.append([[9, -1, -5]])  # return 3
    t_case.append([[-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]])  # return 6

    for tc in t_case:
        print(solution(*tc))
