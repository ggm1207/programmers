import math

def solution(n, times):
    answer = 0

    left = min(times) * math.ceil(n / len(times))
    right = max(times) * math.ceil(n / len(times))

    def get_pass_n(cur_time):
        return sum([cur_time // time for time in times])
    
    # check_time = 80
    # print(get_pass_n(check_time - 1) + sum([1 for time in times if (check_time % time) == 0]))

    while left <= right:
        mid = (left + right) // 2
        pass_n = get_pass_n(mid - 1)

        if pass_n >= n:
            right = mid - 1
            continue

        pass_n += sum([1 for time in times if (mid % time) == 0])
        answer = mid

        if pass_n >= n:
            break
        else:
            left = mid + 1

    return answer


print(solution(6, [7, 10]))
print(solution(6, [7, 10, 3, 5]))
print(solution(61, [7, 10, 3, 5]))
print(solution(61, [3, 3, 3, 3]))
