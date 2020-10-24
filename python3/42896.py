import heapq
from collections import defaultdict

# 거꾸로 시작을 하면 자연히 왼쪽 값이 최대인 경우가 나오고 그 이후로는 max 에서 갱신됨.
def solution(left, right):
    dp = [[0 for _ in range(len(right) + 1)] for _ in range(len(left) + 1)]
    print(left, right)
    for i in range(len(left) - 1, -1, -1):
        for j in range(len(right) - 1, -1, -1):
            if left[i] > right[j]:
                dp[i][j] = dp[i][j + 1] + right[j]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1])
            print(dp[i][j], end=' ')
    print()
    for d in dp:
        print(d)

    return dp[0][0]


if __name__ == "__main__":
    t_case = []
    t_case.append([[3, 2, 5], [2, 4, 1]])
    t_case.append([[4, 2, 6], [2, 3, 1, 5]])
    t_case.append([[3, 3, 1], [7, 7, 1]])
    t_case.append([[1, 3, 3], [1, 7, 7]])

    for tc in t_case:
        print(solution(*tc))
