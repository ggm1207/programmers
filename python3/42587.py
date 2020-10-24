def solution(priorities, location):
    priorities = [(prior, loc) for loc, prior in enumerate(priorities)]
    priorities = priorities[::-1]
    cnt = 0
    while(priorities):
        J, loc = priorities.pop()

        if not priorities:
            break

        if max(priorities, key=lambda x: x[0])[0] > J:
            priorities = [(J, loc)] + priorities
        else:
            if loc == location:
                break
            cnt += 1
    return cnt + 1


if __name__ == "__main__":
    t_case = []
    t_case.append({'priorities': [2, 1, 3, 2], 'location': 2})
    t_case.append({'priorities': [1, 1, 9, 1, 1, 1], 'location': 0})

    for tc in t_case:
        print(solution(**tc))
