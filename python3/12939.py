def solution(s):
    s = sorted(map(int, s.split(" ")))
    return str(s[0]) + " " + str(s[-1])

if __name__ == "__main__":
    t_case = []
    t_case.append(["1 2 3 4"]) # return 1 4
    t_case.append(["-1 -2 -3 -4"]) # return -4 -1
    t_case.append(["-1 -1"]) # return -1 -1

    for tc in t_case:
        print(solution(*tc))
