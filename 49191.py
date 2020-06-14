def solution(n, results):
    wins = {i: set() for i in range(1, n+1)}
    losses = {i: set() for i in range(1, n+1)}
    for i in range(1, n+1):
        for battle in results:
            if battle[0] == i:
                wins[i].add(battle[1])
            if battle[1] == i:
                losses[i].add(battle[0])
        for winner in losses[i]:
            wins[winner].update(wins[i])
        for loser in wins[i]:
            losses[loser].update(losses[i])

    cnt = 0
    for i in range(1, n+1):
        if len(wins[i]) + len(losses[i]) == n-1:
            cnt += 1
    return cnt


if __name__ == "__main__":
    t_case = []
    t_case.append([5 ,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]])

    for tc in t_case:
        print(solution(*tc))
