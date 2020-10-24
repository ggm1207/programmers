from itertools import permutations


def is_prime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return 0
    return 1


def solution(numbers):
    num_len = len(numbers)
    visited = {}
    answer = 0
    for nl in range(1, num_len+1):
        for num in permutations(numbers, nl):
            inum = int(''.join(num))
            if visited.get(inum, True):
                visited[inum] = False
                if inum == 1 or inum == 0:
                    continue
                answer += is_prime(inum)
    return answer


def best_solution(n):  # 에라토스테네스의 체를 set 으로 구현한 코드. good
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


if __name__ == "__main__":
    t_case = []
    t_case.append("17")
    t_case.append("011")

    for tc in t_case:
        print(best_solution(tc))
