# 카탈란 수?
def get_comb(n):
    for i in range(1, n // 2 + 1):
        yield (i, n - i)


def solution(n):
    n_list = [set() for _ in range(n)]
    n_list[0].add("()")

    for num in range(2, n + 1):
        prev_parenthese = n_list[num - 2]

        for paren in prev_parenthese:
            n_list[num - 1].add("(" + paren + ")")

        for nl, nr in get_comb(num):
            nl_paren = n_list[nl - 1]
            nr_paren = n_list[nr - 1]

            for nl_p in nl_paren:
                for nr_p in nr_paren:
                    n_list[num - 1].add(nl_p + nr_p)
                    n_list[num - 1].add(nr_p + nl_p)

    return len(n_list[n - 1])


import math

# catalan(n) = (2n)! / (n! * (n+1)!)
#            = prod(2n ... (n+2)) / prod(n ... 1)
#            = prod(2n ... (n+2)) / prod(n ... 1)


def catalan(n):
    return int(math.prod(range(n + 2, 2 * n + 1)) / math.prod(range(1, n + 1)))


if __name__ == "__main__":
    t_case = []
    t_case.append([2])  # return 2
    t_case.append([3])  # return 5
    t_case.append([4])  # return 5
    t_case.append([14])  # return 5
    t_case.append([44])  # return 5

    for tc in t_case:
        # print(solution(*tc))
        print(catalan(*tc))
