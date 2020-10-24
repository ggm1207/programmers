# parametic search, binary search
import math


def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    dist = [rocks[0]]

    for ri in range(len(rocks) - 1):
        dist.append(rocks[ri + 1] - rocks[ri])
    dist.append(distance - rocks[-1])

    left, right = min(dist), distance

    while left <= right:
        cnt, prev = 0, 0
        mid = (left + right) // 2

        for rock in rocks:
            if rock - prev < mid:
                cnt += 1
            else:
                prev = rock

        if distance - prev < mid:
            cnt += 1

        if cnt <= n:
            if mid > answer:
                answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
print()
print(solution(25, [2, 14, 11, 21, 17, 24], 2))
