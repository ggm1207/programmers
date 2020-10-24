from collections import deque


def solution(people, limit):
    people, answer = deque(sorted(people)), 0
    while(people):
        if len(people) <= 1:
            answer += 1
            break
        skinny = people.popleft()
        while(people):
            fat = people.pop()
            answer += 1
            if fat + skinny <= limit:
                break
            if len(people) == 0:
                answer += 1
    return answer


if __name__ == "__main__":
    t_case = []
    t_case.append([[70, 50, 80, 50], 100])
    t_case.append([[70, 80, 50], 100])
    for tc in t_case:
        print(solution(*tc))
