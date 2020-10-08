def solution(numbers):
    answer = set()
    n = len(numbers)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            answer.add(numbers[i] + numbers[j])

    return sorted(answer)


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
