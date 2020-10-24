# 1. 높은 값을 줄여야 하는 간단한 문제.. But 시간 복잡도 생각하면 어케 될지 모름
# 2. 생각해라 할 수 있다.

def solution(n, works):
    works = sorted(works, reverse=True)
    tot = 0    
    for idx in range(len(works)-1):
        sub_max = works[idx] - works[idx+1]

        if sub_max * ( idx + 1 ) > n:
            break
            
        works[:idx+1] = [works[idx+1]] * ( idx + 1 )
        tot += ( sub_max * ( idx + 1 ))
        n -= sub_max * ( idx + 1 )
    
    idx = works.count(works[0])
    if n:
        m, r = divmod(n, idx)
        works[:idx] = map(lambda x: x-m, works[:idx])
        works[:r] = map(lambda x: x-1, works[:r])
    return sum(map(lambda x: max(x, 0)**2, works))


if __name__ == "__main__":
    t_case = []
    t_case.append([4, [4, 3, 3]])
    t_case.append([1, [2, 1, 2]])
    t_case.append([3, [1, 1]])
    t_case.append([7, [1, 1]])
    # t_case.append([40, [999, 998, 997, 996, 995, 30]])
    # t_case.append([41, [999, 998, 997, 996, 995, 30]])
    # t_case.append([44, [999, 998, 997, 996, 995, 30]])

    for tc in t_case:
        print(solution(*tc))
