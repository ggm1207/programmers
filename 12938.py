def solution(n, s):
    m, r = divmod(s, n)
    answer = [m for _ in range(n)]
    if m == 0:
        return [-1]
    else:
        answer[-r:] = list(map(lambda x: x+1, answer[-r:]))
    return answer

if __name__ == "__main__":
    t_case = []
    t_case.append([2,9]) # return [4, 5]
    t_case.append([2,1]) # return [-1]
    t_case.append([2,8]) # return [4, 4]
    t_case.append([3,9])
    # t_case.append([10000, 10004])
    # t_case.append([10000, 100000000])

    for tc in t_case:
        print(solution(*tc))
