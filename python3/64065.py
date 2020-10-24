def solution(s):
    s_tuple = sorted(s[2:-2].split('},{'), key=len)
    answer = [int(s_tuple[0])]
    for s_tup in s_tuple[1:]:
        s_tup = list(map(int, s_tup.split(',')))
        for ans in answer:
            if ans in s_tup:
                s_tup.remove(ans)
        answer += s_tup
    return answer

import re
from collections import Counter

def best_solution(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))


if __name__ == "__main__":
    t_case = []
    t_case.append("{{2},{2,1},{2,1,3},{2,1,3,4}}")
    t_case.append("{{1,2,3},{2,1},{1,2,4,3},{2}}")
    t_case.append("{{20,111},{111}}")
    t_case.append("{{123}}")
    t_case.append("{{4,2,3},{3},{2,3,4,1},{2,3}}")
    
    for tc in t_case:
        print(best_solution(tc))
