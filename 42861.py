def solution(n, costs):  # kruskal algorithm
    answer = 0
    costs.sort(key = lambda x: x[2])
    connection = set([costs[0][0]])
    while len(connection) != n:
        for i, cost in enumerate(costs):
            if (cost[0] in connection) and (cost[1] in connection): continue
            if (cost[0] in connection) or (cost[1] in connection):
                answer += cost[2]
                connection.add(cost[0])
                connection.add(cost[1])
                costs.pop(i)
                break
    return answer

if __name__ == "__main__":
    t_case = []
    t_case.append([4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]])

    for tc in t_case:
        print(solution(*tc))
    
