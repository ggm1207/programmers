# 0으로 된 도로에 숫자 블록을 설치하기로 하였다.
# 블록 규칙. a(n) = what's?


def get_block(num):
    if num <= 3:  # 1, 2, 3
        return num // 2

    result = 1
    for prime in range(2, int(num ** 0.5 + 1.5)):
        if num % prime != 0:
            continue

        result = num // prime

        if result > 10000000:
            continue

        break

    if result > 10000000:
        return 1

    return result


def solution(begin, end):
    total_len = end - begin + 1
    answer = [0] * total_len

    for idx in range(begin, end + 1):
        block = get_block(idx)
        arr_idx = idx - begin
        answer[arr_idx] = block

    return answer


if __name__ == "__main__":
    t_case = []
    t_case.append([1, 10])  # return [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]
    t_case.append([23, 39])
    t_case.append([999999999, 1000000000])

    for tc in t_case:
        print(solution(*tc))
