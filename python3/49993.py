def check(skill, skill_tree):
    skill_idx = 0

    for skill_ in skill_tree:
        if skill_idx >= len(skill):
            break

        if skill_ in skill and skill_ != skill[skill_idx]:
            return False

        if skill_ == skill[skill_idx]:
            skill_idx += 1

    return True


def solution_v2(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        answer += check(skill, skill_tree)

    return answer


def solution(skill, skill_trees):
    answer = len(skill_trees)

    for skill_tree in skill_trees:
        stack = list(skill[::-1])

        for my_skill in skill_tree:
            if len(stack) == 0:
                continue

            if my_skill in stack and stack[-1] != my_skill:
                answer -= 1
                break

            if my_skill in stack and stack[-1] == my_skill:
                stack.pop()

    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))
