# Paremetic Search.. What is it?


def solution(n, cores):
    # left: 모든 core가 작은 값일 경우, right: 작은 core가 모든 작업을 처리하는 경우
    left, right = min(cores) * n // len(cores), min(cores) * n
    n -= len(cores)

    def get_task(time):
        return sum(map(lambda core: time // core, cores))

    while left <= right:
        mid = (left + right) // 2
        task_num = get_task(mid - 1)

        if task_num >= n:
            right = mid - 1
            continue
        
        for idx, core in enumerate(cores):
            if mid % core == 0:
                task_num += 1

            if task_num == n:
                answer = idx + 1
                return answer

        if task_num < n:
            left = mid + 1


if __name__ == "__main__":
    print(solution(6, [1, 2, 3]))
    print(solution(7, [1, 2, 3]))
    print(solution(8, [1, 2, 3]))
    print(solution(9, [1, 2, 3]))
    print(solution(10, [1, 2, 3]))
    print(solution(10, [1, 1, 1, 1]))
    print(solution(10, [1, 1, 1, 1]))
