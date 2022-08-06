def solution(arr1, arr2):
    return [[a1 + a2 for a1, a2 in zip(ar1, ar2)] for ar1, ar2 in zip(arr1, arr2)]


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(solution([[1], [2]], [[3], [4]]))
