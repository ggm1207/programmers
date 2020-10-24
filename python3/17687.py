def solution(n, t, m, p):
    num_dicts = {i: format(i, 'X') for i in range(16)}

    def getN(num):
        nn = ''
        while num:
            nn += num_dicts[num % n]
            num = num // n
        return nn[::-1] if nn else '0'

    def getStr():
        return ''.join([getN(i) for i in range(30000)]) # 30000 하니깐 통과 ㅋㅋ 이렇게 풀면 안됨.

    answer = getStr()[p-1::m][:t]
    return answer


if __name__ == "__main__":
    t_case = []
    t_case.append([2, 4, 2, 1])
    t_case.append([3, 16, 2, 1])
    t_case.append([16, 16, 2, 1])
    t_case.append([16, 16, 2, 2])

    for tc in t_case:
        print(solution(*tc))
