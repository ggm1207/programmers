def solution(seoul):
    answer = "김서방은 {}에 있다".format(seoul.index("Kim"))
    return answer


if __name__ == "__main__":
    t_case = []
    t_case.append([["Jane", "Kim"]])  # return 김서방은 1에 있다

    for tc in t_case:
        print(solution(*tc))
