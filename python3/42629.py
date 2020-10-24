import heapq

def solution(stock, dates, supplies, k):
            
    # 현재 stock 에서 받을 수 있는 날짜 중 최대값
    # 늘어난 날짜 queue 에 삽입
    queue = []
    total_stock = stock
    answer = 0

    def push2heap():
        nonlocal dates, supplies
        for idx, d in enumerate(dates):
            if d <= total_stock:
                heapq.heappush(queue, (-supplies[idx], d))
                continue
            break
        dates, supplies = dates[idx:], supplies[idx:]

    while total_stock < k:
        push2heap()
        supply, date = heapq.heappop(queue)
        total_stock -= supply
        answer += 1

    return answer


if __name__ == "__main__":
    t_case = []
    t_case.append([4, [4, 10, 15], [20, 5, 10], 30])

    for tc in t_case:
        print(solution(*tc))
