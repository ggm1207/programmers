def solution(n, money):
    answer = 0
    d = [0] * (n + 1)
    d[0] = 1
    m = money[0]

    while m <= n:
        d[m] = 1
        m += money[0]

    for j in range(1, len(money)):
        for i in range(n+1):
            if i >= money[j]:
                d[i] += d[i - money[j]] % 1000000007

    answer = d[n]
    return answer


if __name__ == "__main__":
    t_case = []
    t_case.append([5, [1, 2, 5]])  # return 4

    for tc in t_case:
        print(solution(*tc))
