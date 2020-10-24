def solution(A, B):
    A, B = sorted(A), sorted(B)
    ai, bi = 0, 0
    score = 0 
    while ai < len(A) and bi < len(B):
        if A[ai] < B[bi]: # B[bi] marking A[ai]
            score += 1
            ai, bi = ai + 1, bi + 1
            continue

        if A[ai] >= B[bi]:
            bi += 1

    return score

if __name__ == "__main__":
    t_case = []
    t_case.append([[5,1,3,7],[2,2,6,8]]) # return 3
    t_case.append([[2,2,2,2],[1,1,1,1]]) # return 0

    for tc in t_case:
        print(solution(*tc))
