def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    connection = set([costs[0][0]])
    while len(connection) != n:
        for i, cost in enumerate(costs):
            if (cost[0] in connection) and (cost[1] in connection): continue
            if (cost[0] in connection) or (cost[1] in connection):
                answer += cost[2]
                connection.update([cost[0], cost[1]])
                costs.pop(i)
                break
    return answer

if __name__ == "__main__":
    t_case = []
    t_case.append([4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]])
    t_case.append([4, [[0,1,1],[0,2,2],[1,2,5],[1,3,2],[2,3,1]]])
    t_case.append([5, [[0,1,1],[0,2,3],[1,2,5],[1,3,3],[2,3,1],[1,4,1],[4,0,2]]])
    t_case.append([5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]])
    t_case.append([5, [[0,1,1],[0,4,5],[2,4,1],[2,3,1],[3,4,1]]])

    for tc in t_case:
        print(solution(*tc))

