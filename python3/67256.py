def solution(numbers, hand):
    answer = ""
    keypad = { k: divmod(i, 3) for i, k in zip(range(12), "1 2 3 4 5 6 7 8 9 * 0 #".split(" "))}

    def get_dist(to, fr):
        to = keypad[str(to)]
        fr = keypad[str(fr)]
        return abs(to[0] - fr[0]) + abs(to[1] - fr[1])

    left_pos = "*"
    right_pos = "#"

    for number in numbers: 
        left_dist = get_dist(left_pos, number)
        right_dist = get_dist(right_pos, number)

        if number in [1, 4, 7]:
            answer += "L"
        elif number in [3, 6, 9]:
            answer += "R"
        else:
            if left_dist < right_dist:
                answer += "L"
            elif left_dist > right_dist:
                answer += "R"
            else:
                answer += "L" if hand == "left" else "R"
            
        if answer[-1] == "L":
            left_pos = number
        else:
            right_pos = number

    return answer


if __name__ == "__main__":
    t_case = []
    t_case.append(
        [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"]
    )  # return "LRLLLRLLRRL"
    t_case.append(
        [[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"]
    )  # return "LRLLRRLLLRR"
    t_case.append(
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"]
    )  # return "LLRLLRLLRL"

    for tc in t_case:
        print(solution(*tc))
