import math


def solution(w, h):
    return w*h - (w+h-math.gcd(w, h))


if __name__ == "__main__":
    t_case = []
    t_case.append({'w': 8, 'h': 12})
    t_case.append({'w': 8, 'h': 1})
    t_case.append({'w': 4, 'h': 1})
    t_case.append({'w': 8, 'h': 2})
    t_case.append({'w': 8, 'h': 8})

    for tc in t_case:
        print(solution(**tc))
