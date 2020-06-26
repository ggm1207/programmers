def solution(s):
    s = list(s)[::-1]
    stack = []
    while s:
        stack.append(s.pop())
        if len(stack) > 1:
            if stack[-1] == ")":
                stack.pop()
                stack.pop()
    return False if stack else True


if __name__ == "__main__":
    t_case = []
    t_case.append("()()")
    t_case.append("(())()")
    t_case.append(")()(")
    t_case.append("(()(")

    for tc in t_case:
        print(solution(tc))
