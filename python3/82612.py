def solution(price, money, count):
    total_money = sum([price * i for i in range(1, count + 1)])
    return max(total_money - money, 0)


print(solution(3, 20, 4))
