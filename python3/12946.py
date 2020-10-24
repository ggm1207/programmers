def solution(n):
    answer = []
    nums = set([1, 2, 3])

    def dfs(fr, to, depth):
        last = nums.difference([fr, to]).pop()
        if depth == 1:
            answer.append([fr, to])
            return

        dfs(fr, last, depth-1)
        answer.append([fr, to])
        dfs(last, to, depth-1)

    dfs(1, 3, n)

    return answer

if __name__ == "__main__":
    t_case = []
    t_case.append([2]) # return [ [1,2], [1,3], [2,3] ]
    t_case.append([3]) # return [ [1,2], [1,3], [2,3] ]
    t_case.append([4]) # return [ [1,2], [1,3], [2,3] ]

    for tc in t_case:
        print(solution(*tc))
