# DP is the key for solution, right?
from sys import setrecursionlimit

setrecursionlimit(100000)


# This code is trash, but right
def trash_solution(arr):
    answer = 0

    def dfs(eq_arr):
        if len(eq_arr) <= 3:
            return eval("".join(eq_arr))

        results = []
        for i in range(0, len(eq_arr) - 1, 2):
            sv, seq = eval("".join(eq_arr[i : i + 3])), eq_arr[i + 3 :]
            seq = eq_arr[:i] + [str(sv)] + seq
            results.append(dfs(seq))

        return max(results)

    answer = dfs(arr)
    return answer


def solution(arr):
    op, nums = arr[1::2], list(map(int, arr[::2]))
    MAX_V = 987654321
    alen = len(nums)
    dp = [[[-MAX_V, MAX_V] for _ in range(alen)] for _ in range(alen)]

    def max_mul(i, k, j):  # dp[i][k] * dp[k+1][j]
        return (
            dp[i][k][0] + dp[k + 1][j][0]
            if op[k] == "+"
            else dp[i][k][0] - dp[k + 1][j][1]
        )

    def min_mul(i, k, j):  # dp[i][k] * dp[k+1][j]
        return (
            dp[i][k][1] + dp[k + 1][j][1]
            if op[k] == "+"
            else dp[i][k][1] - dp[k + 1][j][0]
        )

    dp[0][0][0] = nums[0]
    dp[0][0][1] = nums[0]
    for i in range(1, alen):
        dp[i][i][0] = nums[i]
        dp[i][i][1] = nums[i]
        dp[i - 1][i][0] = max_mul(i - 1, i - 1, i)
        dp[i - 1][i][1] = min_mul(i - 1, i - 1, i)

    for dist in range(2, alen):
        for i in range(0, alen - dist):
            for k in range(i, i + dist):
                dp[i][i + dist][0] = max(dp[i][i + dist][0], max_mul(i, k, i + dist))
                dp[i][i + dist][1] = min(dp[i][i + dist][1], min_mul(i, k, i + dist))
    
    for d in dp:
        print(d)

    return dp[0][-1][0]


# print(trash_solution(["3", "-", "3"]))
print(solution(["3", "+", "31"]))
# print(trash_solution(["334", "-", "0"]))
# print(solution(["334", "-", "334", "-", "334"]))
print(solution(["334", "-", "334", "-", "334", "-", "334"]))

# print(trash_solution(["1", "-", "3", "+", "5", "-", "8"]))
# print(solution(["1", "-", "3", "+", "5", "-", "8"]))
# print(trash_solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))
# print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))
# print(trash_solution(["5", "-", "3", "+", "1", "+", "2", "-", "4", "-", "2"]))
# print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4", "-", "2"]))
