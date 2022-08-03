def solution(n):
    divisor = []

    for k in range(1, int(n**0.5 + 1.5)):
        if n % k == 0:
            divisor.append(k)

    divisor += list(map(lambda d: n // d, divisor))
    return sum(set(divisor))


print(solution(0))
print(solution(1))
print(solution(2))
print(solution(12))
print(solution(5))
