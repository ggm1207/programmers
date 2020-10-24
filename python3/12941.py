def solution(A,B):
    return sum(map(lambda x, y: x * y, sorted(A), sorted(B, reverse=True)))


if __name__ == "__main__":
    t_case = []
    t_case.append([[1, 4, 2],[5, 4, 4]]) # return 29
    t_case.append([[1,2],[3,4]]) # return 10

    for tc in t_case:
        print(solution(*tc))
