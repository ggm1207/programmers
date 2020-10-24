import re
from itertools import permutations

def solution(expression):
    nums, ops = re.findall("\d+", expression), re.findall("[-+*]", expression)
    max_ = 0

    for ord_ops in permutations(set(ops), len(set(ops))):
        nums_cp, ops_cp = nums[::], ops[::]
        ord_ops = list(ord_ops)

        while ord_ops:
            op = ord_ops.pop()
        
            while op in ops_cp:
                op_idx = ops_cp.index(op)
                ops_cp.pop(op_idx)
                nums_cp = nums_cp[:op_idx] + [str(eval("".join([nums_cp[op_idx], op, nums_cp[op_idx+1]])))] + nums_cp[op_idx+2:]
        max_ = max(abs(int(nums_cp[0])), max_)
    return max_


if __name__ == "__main__":
    t_case = []
    t_case.append(["100-200*300-500+20"])  # return 60420
    t_case.append(["50*6-3*2"])  # return 300

    for tc in t_case:
        print(solution(*tc))
