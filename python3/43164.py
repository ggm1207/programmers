from collections import defaultdict

def solution(tickets):
    airto = defaultdict(list)
    answer_len = len(tickets) + 1

    for to, fo in tickets:
        airto[to].append(fo)

    for k, v in airto.items():
        airto[k] = sorted(v)
        
    start = "ICN" 
    answer = [start]
    real_answer = []

    def dfs(start):
        nonlocal real_answer
        if len(answer) == answer_len:
            real_answer = answer[:]
            return

        if real_answer:
            return
        
        nexts = airto[start]
        for idx, nex in enumerate(nexts):
            answer.append(nex)
            airto[start] = nexts[:idx] + nexts[idx+1:]
            dfs(nex)
            answer.pop()
            airto[start] = nexts

    dfs(start)

    return real_answer

if __name__ == "__main__":
    t_case = []
    t_case.append([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
    t_case.append([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])

    for tc in t_case:
        print(solution(tc))
