def solution(n):
    n_cnt = bin(n).count('1')
    n += 1
    while n_cnt != bin(n).count('1'):
        n += 1
    return n


if __name__ == "__main__":
    t_case = []
    t_case.append(78)
    t_case.append(15)

    for tc in t_case:
        print(solution(tc))
