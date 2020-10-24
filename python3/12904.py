def solution(s):
    dp = [[False for _ in range(len(s))] for _ in range(len(s))]
    max_ = 0

    for i in range(len(s)):
        for j in range(len(s)):
            if i == j:
                dp[i][j] = True
    
    for start in range(len(s) - 1):
        dp[start][start + 1] = s[start] == s[start + 1]
        if dp[start][start + 1]:
            max_ = 2

    for width in range(2, len(s)):
        for start in range(len(s) - width):
            dp[start][start + width] = (s[start] == s[start + width] and dp[start+1][start + width - 1])
            if dp[start][start + width]:
                max_ = max(max_, width + 1)
    return max_ if max_ else 1


from collections import defaultdict
def solution(s):
    dp = defaultdict(bool)
    s_len = len(s)
    max_ = 0

    for i in range(s_len):
        dp[i, i] = True

    for width in range(1, s_len):
        for start in range(s_len - width):
            end = start + width
            dp[start, end] = (s[start] == s[end])
            
            if width != 1:
                dp[start, end] = dp[start, end] and dp[start + 1, end - 1]

            if dp[start, end]:
                max_ = max(max_, width + 1)
    return max_ if max_ else 1 

from difflib import SequenceMatcher as SM

def best_solution(s):
    return SM(None, s, s[::-1]).find_longest_match(0, len(s), 0, len(s)).size

if __name__ == "__main__":
    t_case = []
    t_case.append("abcdcba")
    t_case.append("abacde")
    t_case.append("aa")
    t_case.append("aaaa")
    t_case.append("a"*2500)
    t_case.append("a")
    t_case.append("a")

    for tc in t_case:
        # print(solution(tc))
        print(best_solution(tc))
        print(copy_best_solution(tc))
