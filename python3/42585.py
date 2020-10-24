def solution(arrangement):
    answer = 0
    stack = []
    arrangement = list(arrangement[::-1])
    IRON, LASER = 0, 1
    NOW = 0
    while(arrangement):
        arg = arrangement.pop()
        if arg == '(':
            stack.append(arg)
            NOW = IRON
        elif arg == ')':
            if NOW == IRON:
                stack.pop()
                answer += len(stack)
                NOW = LASER
                continue
            stack.pop()
            answer += 1
    return answer


if __name__ == "__main__":
    print(solution("()(((()())(())()))(())"))
