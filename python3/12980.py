def solution(n):
    return bin(n).count('1')

if __name__ == "__main__":
    t_case = []
    t_case.append([5]) # return 2
    t_case.append([6]) # return 2
    t_case.append([5000]) # return 5

    for tc in t_case:
        print(solution(*tc))
