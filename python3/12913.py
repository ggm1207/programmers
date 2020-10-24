def solution(land):
    for n in range(1, len(land)):
        for i in range(4):
            land[n][i] += max(land[n-1][:i] + land[n-1][i+1:])
    return max(land[-1])

if __name__ == "__main__":
    t_case = []
    t_case.append([[[1,2,3,5],[5,6,7,8],[4,3,2,1]]]) # return 16

    for tc in t_case:
        print(solution(*tc))
