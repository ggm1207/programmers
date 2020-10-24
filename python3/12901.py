import datetime


def solution(a, b):
    week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    idx = datetime.datetime(2016, a, b).weekday()
    return week[idx]


if __name__ == "__main__":
    t_case = []
    t_case.append([5, 24])
    for tc in t_case:
        print(solution(*tc))
