def solution(n, lost, reserve):
    answer = 0
    for l in lost:
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)
    cl = [1 for _ in range(n)]
    for r in reserve:
        cl[r-1] += 1 

    for l in lost:
        cl[l-1] -= 1 
    
    for i, c in enumerate(cl):
        if c == 0:
            lc = max(i-1,0)
            if cl[lc] == 2:
                cl[lc] -= 1
                cl[i] += 1
                continue
            rc = min(n-1,i+1)
            if cl[rc] == 2:
                cl[rc] -= 1
                cl[i] += 1
    cl = map(bool, cl)
    answer = sum(cl)
    return answer


if __name__ == "__main__":
    t_case = []
    t_case.append([5,[2,4],[1,3,5]])
    t_case.append([5,[2,4],[3]])
    t_case.append([3,[3],[1]])
    for tc in t_case:
        print(solution(*tc))
