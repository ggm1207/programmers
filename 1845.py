def solution(nums):
    N = len(nums) // 2
    answer = min(N, len(set(nums)))
    return answer


if __name__ == "__main__":
    t_cases = []
    t_cases.append([[3, 1, 2, 3]])
    t_cases.append([[3, 3, 3, 2, 2, 4]])
    t_cases.append([[3, 3, 3, 2, 2, 2]])

    for tc in t_cases:
        print(solution(*tc))
