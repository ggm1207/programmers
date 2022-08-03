def solution(s, n):
    lower = lambda c: chr((ord(c) - ord("a") + n) % 26 + ord("a"))
    upper = lambda c: chr((ord(c) - ord("A") + n) % 26 + ord("A"))
    shift = lambda c: lower(c) if c.islower() else upper(c) if c.isalpha() else c
    return "".join(map(lambda c: shift(c), s))


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
