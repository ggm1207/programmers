import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while len(scoville) > 1:
        food_1 = heapq.heappop(scoville)
        food_2 = heapq.heappop(scoville)
        if food_2 >= food_1 >= K:
            return cnt
        heapq.heappush(scoville, food_1 + food_2 * 2)
        cnt += 1
    if len(scoville) == 1 and scoville[0] >= K:
        return 1
    return -1


if __name__ == "__main__":
    t_case = []
    t_case.append([[1, 2, 3, 9, 10, 12], 7])

    for tc in t_case:
        print(solution(*tc))
