def solution(s):
    answer = 0
    stack = [0]
    s = list(s)
    while s:
        stack.append(s.pop())
        if stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    return int(stack[-1] == 0)

if __name__ == "__main__":
    t_case = []
    t_case.append("baabaa")
    t_case.append("cdcd")

    for tc in t_case:
        print(solution(tc))

