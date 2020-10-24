from itertools import permutations, product

def solution(numbers, target): 
    result = [0 for _ in range(2**(len(numbers)+1) + 2)]
    for depth, n in enumerate(numbers):
        pr = 2 ** depth if depth != 0 else 1 
        for p in range(pr, pr*2):
            result[p*2] = result[p] + n
            result[p*2+1] = result[p] - n  
    return result[pr*2:].count(target) 

print(solution([1,1,1,1,1],3))
