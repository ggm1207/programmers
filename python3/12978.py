def solution(N, road, K):
    dp = [[0 for _ in range(N)] for _ in range(N)]
    for n1, n2, w in road:
        dp[n1-1][n2-1] = min(w, dp[n1-1][n2-1]) if dp[n1-1][n2-1] != 0 else w
        dp[n2-1][n1-1] = min(w, dp[n2-1][n1-1]) if dp[n2-1][n1-1] != 0 else w
    N_cp = N 
    while N_cp:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if k == i or k == j:
                        continue
                    if not dp[i][k] or not dp[k][j]: # 이어지는 도로가 없다면
                        continue
                    if dp[i][j] == 0:
                        dp[i][j] = dp[i][k] + dp[k][j]
                    else:
                        dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])
                    # print(i, j, dp[i][j])
        N_cp -= 1
    return len(list(filter(lambda x: x <= K, dp[0][1:]))) + 1


if __name__ == "__main__":
    t_case = []
    t_case.append([5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3])
    t_case.append([6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4])

    for tc in t_case:
        print(solution(*tc))
