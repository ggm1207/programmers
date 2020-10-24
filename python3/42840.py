from itertools import cycle

def solution(answers):
    pep_1 = cycle([1,2,3,4,5])  
    pep_2 = cycle([2,1,2,3,2,4,2,5])    
    pep_3 = cycle([3,3,1,1,2,2,4,4,5,5])
    count = [0 for _ in range(3)]
    for ans in answers:
        p1, p2, p3 = map(next, [pep_1, pep_2, pep_3])
        count = list(map(lambda x, cnt: (x == ans) + cnt, [p1, p2, p3], count))
    max_cnt = max(count)
    count = map(lambda x, idx: idx if x == max_cnt else 0, count, range(1, 4))
    count = filter(bool, count) 
    return sorted(count)

if __name__ == "__main__":
    t_case = []
    t_case.append([[1,2,3,4,5]])
    t_case.append([[1,3,2,4,2]])
    for tc in t_case:
        print(solution(*tc))
