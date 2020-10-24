def solution(budgets, M):
    budgets = sorted(budgets)
    budgets_len = len(budgets)
    avg = M / budgets_len
    over_idx = 0
    while(budgets[over_idx] <= avg):
        M -= budgets[over_idx]
        over_idx += 1
        if budgets_len == over_idx:
            return max(budgets)
        avg = M / (budgets_len - over_idx) 
    return int(avg)

# Other solution in Programmers
# more slower than my solution, HA HA HA!
def solution(budgets, M):
    start, end = 0, max(budgets)
    while start <= end:
        mid = (start + end) // 2
        temp = sum([budget if budget <= mid else mid for budget in budgets])
        print(mid, temp, M, start, end)
        if temp > M: end = mid - 1
        elif temp < M: start = mid + 1
        else: return mid
    return (start + end) // 2

if __name__=="__main__":
    t_case = []
    t_case.append([[120, 110, 140, 150], 485])
    for tc in t_case:
        print(solution(*tc))
