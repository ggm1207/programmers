# dp[i] = max(dp[i-1], money[i] + dp[i-2])
# 집이 3개만 있을 때를 가정하고 생각하면 점화식 세우기 쉽다.


def solution(money):
    answer = 0
    m_len = len(money)
    dp1 = [0] * m_len

    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, m_len-1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    dp2 = [0] * m_len
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, m_len):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    answer = max(dp1 + dp2)
    return answer


if __name__ == "__main__":
    t_case = []
    # t_case.append([[1, 2, 3, 1]])  # return 4
    t_case.append([[2, 2, 5, 1, 5]])  # return 10

    for tc in t_case:
        print(solution(*tc))
