def solution(arr):
    min_v = min(arr)
    return [-1] if len(arr) == 1 else [v for v in arr if v != min_v]


print(solution([4, 3, 2, 1]))
print(solution([10]))
