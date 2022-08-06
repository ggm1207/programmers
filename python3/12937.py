def solution(num):
    return ["Even", "Odd"][num % 2]


def solution_v2(num):
    return ["Even", "Odd"][num & 1]


print(solution(3))
print(solution(4))
