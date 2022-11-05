"""
    - 두 선수가 먹는 음식의 종류와 양이 같아야 하며
    - 음식을 먹는 순서도 같아야 함
    - 칼로리가 낮은 음식을 먼저 먹을 수 있게 배치
"""


def solution(food):
    food = list(map(lambda food_: food_ // 2, food))
    food = "".join([str(i) * food_ for i, food_ in enumerate(food[1:], start=1)])
    answer = food + "0" + food[::-1]
    return answer


print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))
