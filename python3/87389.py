def solution(n):
    n -= 1

    for k in range(2, n // 2 + 1):
        if n % k == 0:
            return k

    return n


print(solution(10))
print(solution(12))
