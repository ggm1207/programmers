def solution(s):
    return ' '.join(map(lambda x: x[0].upper() + x[1:].lower() if len(x) > 1 else x.upper(), s.split(" ")))

if __name__ == "__main__":
    t_case = []
    t_case.append("3people unFollowed me")
    t_case.append("peo3ple unFollowed me")
    t_case.append("for the last week")
    t_case.append("f")
    t_case.append("3")

    for tc in t_case:
        print(solution(tc))
