def solution(x, n):
    if x == 0:
        return [0] * n
    return list(range(x, x * (n + 1), x))


print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))
print(solution(-4, 1))
print(solution(0, 2))
