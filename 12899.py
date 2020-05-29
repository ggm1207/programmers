def solution(n):
    answer = ''
    ad, sec = 3, 0
    while True:
        if n <= ad: break
        sec += 1
        ad += 3 ** (sec + 1)    
    sec_total_num = 3 ** (sec + 1)
    n_pos = n - (ad - (3 ** (sec + 1)))
    sec_1, sec_2 = sec_total_num // 3, (sec_total_num // 3) * 2
    for _ in range(sec+1):
        if n_pos <= sec_1:
            answer += '1'
        elif n_pos <= sec_2:
            answer += '2'
            n_pos -= (sec_total_num // 3)
        else:
            answer += '4'
            n_pos -= (sec_total_num // 3) * 2
        sec_total_num //= 3 
        sec_1, sec_2 = sec_total_num // 3, (sec_total_num // 3) * 2
    return answer


def best_solution(n):
    if n <= 3:
        return '124'[n-1]
    q, r = divmod(n-1, 3)
    return best_solution(q) + '124'[r]

if __name__ == "__main__":
    t_case = [i for i in range(1, 30)]
    for tc in t_case:
        print(solution(tc))
    print(solution(500000000))
    print(best_solution(500000000))
        
