def solution(x):
    return False if x % eval("+".join(list(str(x)))) else True


print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))
