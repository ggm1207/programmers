import sys
sys.setrecursionlimit(20)

answer = {2**k: k for k in range(1, 21)}

def solution(n,a,b):
    MIS = lambda x: n // 2 if x % (n // 2) == 0 else x % (n // 2)
    a, b = sorted([a, b])
    return answer[n] if ( a  <= n // 2 < b  ) else solution(n // 2, MIS(a), MIS(b))

def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()

if __name__ == "__main__":
    t_case = []
    t_case.append([8,4,7]) # return 3
    t_case.append([4,1,2]) # return 1
    t_case.append([2,1,2]) # return 1
    t_case.append([8,6,7]) # return 2

    for tc in t_case:
        print(solution(*tc))
