# M[i][j] = minimum(M[i][k] + M[k+1][j] + d(i-1)*d(k)*d(j) ( i <= k <= j-1 )
# M[i][j] = 0 ( if i == j )
def solution(matrix_sizes):
    M = [[0] * len(matrix_sizes) for _ in matrix_sizes]
    D = [matrix_sizes[0][0]] + list(list(zip(*matrix_sizes))[1])

    MIJ = lambda i, j: 0 if i == j else min([M[i][k] + M[k+1][j] + D[i-1] * D[k] * D[j] for k in range(i, j)])

    for nt in range(len(matrix_sizes) - 1):
        for mi in range(len(matrix_sizes) - nt - 1):
            mj = mi + nt + 1
            M[mi][mj] = MIJ(mi, mj)
                
    return M[0][-1]

if __name__ == "__main__":
    t_case = []
    t_case.append([[[5,3],[3,10],[10,6]]]) # return 270
    t_case.append([[[20,1],[1,30],[30,10], [10, 10]]]) # return 270

    for tc in t_case:
        print(solution(*tc))
