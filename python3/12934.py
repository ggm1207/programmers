def solution(n):
    answer = n**0.5
    return int(answer + 1) ** 2 if int(answer) == answer else -1


print(solution(121))
print(solution(3))
