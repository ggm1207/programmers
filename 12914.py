def solution(n):
    if n <= 3: return n
    answer = [1, 1] + [0] * (n - 2)
    for idx in range(n-2):
        answer[idx + 1] += answer[idx]
        answer[idx + 2] += answer[idx]
    return sum(answer[-2:]) % 1234567

if __name__ == "__main__":
    t_case = []
    t_case.append([4]) # return 5
    t_case.append([3]) # return 3

    for tc in t_case:
        print(solution(*tc))
