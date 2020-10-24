def solution(number, k):
    answer = ''
    lens = len(number) - k
    number = list(number[::-1])
    stack = [number.pop()]
    while k and number:
        num = number.pop()
        while stack and k:
            if stack[-1] < num:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(num)
    return ''.join(stack + number[::-1])[:lens]


if __name__ == "__main__":
    t_case = []
    t_case.append(["1924", 2])
    t_case.append(["1231234", 3])
    t_case.append(["4177252841", 4])
    t_case.append(["1234", 2])
    t_case.append(["77777", 2])

    for tc in t_case:
        print(solution(*tc))
