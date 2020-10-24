from itertools import combinations

def solution(nums):
    max_num = sum(sorted(nums)[-3:])
    seive = [False, False] + [True] * ( max_num - 1 )
    answer = 0

    for n in range(2, int(max_num ** 0.5 + 1.5)):
        if seive[n]:
            seive[n*2::n] = [False] * ((max_num - n) // n)

    for comb in combinations(nums, 3):
        if seive[sum(comb)]:
            answer += 1

    return answer

if __name__ == "__main__":
    t_case = []
    t_case.append([[1,2,3,4]]) # return 1
    t_case.append([[1,2,7,6,4]]) # return 4

    for tc in t_case:
        print(solution(*tc))
