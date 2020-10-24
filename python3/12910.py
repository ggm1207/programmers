def solution(arr, divisor):
    arr = list(filter(lambda x: not (x % divisor), arr))
    return sorted(arr) if arr else [-1]
