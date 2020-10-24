def solution(n):
    answer = 0
    
    s_idx, e_idx = 1, 2
    sums = 1
    
    while e_idx < n + 2:
        if sums < n:
            sums += e_idx
            e_idx += 1
        elif sums >= n:
            if sums == n:
                answer += 1
            s_idx += 1
            e_idx = s_idx + 1
            sums = s_idx

    return answer

def solution(num):
    return len([i  for i in range(1,num+1,2) if num % i == 0])

if __name__ == "__main__":
    t_case = []
    t_case.append([15]) # return 4

    for tc in t_case:
        print(solution(*tc))
