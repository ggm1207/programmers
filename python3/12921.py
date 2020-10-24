def solution(n):
    seive = [False, False] + [True] * (n - 1)
    for k in range(2, int(n ** 0.5 + 1.5)):
        if seive[k]:
            seive[k*2::k] = [False] * ((n - k) // k)

    return sum(seive)

# 이 함수는 파이썬 스러웠지만 위 함수보다 5배정도 더 느림.
def good_solution(n):
    nums = set(range(2, n+1))
    for num in range(2, int(n ** 0.5 + 1.5)):
        if num in nums:
            nums -= set(range(2*num, n+1, num))

    return len(nums)


if __name__ == "__main__":
    t_case = []
    t_case.append([10]) # return 4
    t_case.append([5]) # return 3
    t_case.append([1000000]) # return 3

    for tc in t_case:
        print(solution(*tc))
        print(good_solution(*tc))
