def gcd(n, m):
    return n if m == 0 else gcd(m, n % m)


def lcm(n, m):
    return n * m // gcd(n, m)


def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    return answer


print(solution(3, 12))
print(solution(2, 5))
