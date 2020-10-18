def solution(stones, k):
    left, right = 1, 200000000
    
    while left <= right:
        mid = (left + right) // 2

        cnt, check = 0, False

        for i in range(len(stones)):
            stone_left_num = stones[i] - mid

            if stone_left_num > 0:
                cnt = 0
                continue

            cnt += 1

            if cnt >= k:
                check = True
                break

        if check:
            right = mid - 1
        else:
            left = mid + 1

    return left

if __name__ == "__main__":
    t_case = []
    t_case.append([[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3])  # return 3
    t_case.append(
                [[1, 1, 1, 1, 2, 4, 5, 3, 2, 1, 4, 2, 5, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 3]
    )
    t_case.append([[200000000 - i for i in range(200000)], 199999])
    t_case.append([[i for i in range(200000)], 199999])

    for tc in t_case:
        print(solution(*tc))
