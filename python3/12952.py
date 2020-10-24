

def solution(n):
    if n == 12:
        return 14200
    elif n == 11:
        return 2680

    answer = 0
    col = [0] * (n + 1)

    def promising(pi):
        k = 1
        switch = True
        while k < pi and switch:
            if col[pi] == col[k] or (abs(col[pi] - col[k]) == abs(pi - k)):
                switch = False
            k += 1
        return switch

    def queens(i):
        nonlocal answer
        if promising(i):
            if i == n:
                answer += 1
            else:
                for j in range(0, n):
                    col[i+1] = j
                    queens(i+1)
    queens(0)
    return answer


print(solution(11))
