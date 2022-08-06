def solution(num):
    task = lambda num: num * 3 + 1 if num % 2 else num // 2

    for i in range(501):
        if num == 1:
            return i

        num = task(num)

    return -1


print(solution(6))
print(solution(16))
print(solution(626331))
