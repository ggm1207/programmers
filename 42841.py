from itertools import permutations

def solution(baseball):
    answer = 0
    baseball = list(map(lambda x: [str(x[0]), x[1], x[2]], baseball))
    for my_num in permutations(list(map(str, range(1, 10))), 3):
        for fr_num, strike, ball in baseball:
            strike_cnt = sum([my_num[i] == fr_num[i] for i in range(3)])
            ball_cnt = len(set(fr_num).intersection(set(my_num))) - strike_cnt
            if ball != ball_cnt or strike != strike_cnt:
                break
        else:
            answer += 1
    return answer


if __name__ == "__main__":
    t_case = []
    t_case.append([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])

    for tc in t_case:
        print(solution(tc))
