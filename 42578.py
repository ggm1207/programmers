from functools import reduce
from collections import defaultdict

mul = lambda lists: reduce(lambda x, y : x * y, lists)

def solution(clothes):
    c_dict = defaultdict(int)
    for ct in clothes:
        c_dict[ct[1]] += 1
    return mul(map(lambda x: x+1, c_dict.values())) - 1

if __name__ == "__main__":
    t_case = []
    t_case.append([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]) 
    t_case.append([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]) 
    t_case.append(t_case[0] + t_case[1])


    for tc in t_case:
        print(solution(tc))
