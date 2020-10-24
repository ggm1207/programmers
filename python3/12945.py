from functools import lru_cache

def solution(n):

    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2: return n
        return fib(n-1) + fib(n-2)

    return [fib(i) for i in range(n+1)][-1] % 1234567


if __name__ == "__main__":
    t_case = []
    t_case.append(3)
    t_case.append(5)

    for tc in t_case:
        print(solution(tc))
