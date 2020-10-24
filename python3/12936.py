import math

def solution(n, k):
    answer = []
    cards = [i + 1 for i in range(n)]
    N = math.factorial(n)

    while n:
        s_range = N // n
        c, r = divmod(k, s_range)
        if r == 0:
            answer.append(cards.pop(c - 1))
        else:
            answer.append(cards.pop(c))

        k = r
        n -= 1
        N = s_range

    return answer

if __name__ == "__main__":
    t_case = []
    t_case.append([3, 5]) # return [3,1,2]

    for tc in t_case:
        print(solution(*tc))
