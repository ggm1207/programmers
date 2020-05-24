def solution(citations):
    n = len(citations)
    max_h = 0
    for h in range(1, n+1):
        h_up = list(filter(lambda x: x >= h, citations))
        if len(h_up) >= h:
            max_h = max(max_h, h)
    return max_h


if __name__ == "__main__":
    t_case = []
    t_case.append([3, 0, 6, 1, 5])

    for tc in t_case:
        print(solution(tc))
