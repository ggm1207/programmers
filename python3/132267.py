"""
    - 단, 보유 중인 빈 병이 2개 미만이면, 콜라를 받을 수 없다.
    - 콜라를 받기 위해 마트에 주어야 하는 병 수 'a'
    - 빈 병 a개를 가져다 주면 마트가 주는 콜라 병 수 'b'
    - 상빈이가 가지고 있는 빈 병의 개수 'n'

    알고리즘

    1. 콜라를 마신다.
    2. 빈병이 생긴다. (남은 빈병이 있을수도 있다.)
    3. 마트로 들고간다.
    4. 콜라가 생긴다. 남은 빈병이 있을수도 있다.

    다른 사람 풀이 (느낌이 안 좋더라니..)
    - solution_v2
"""


def solution(a, b, n):
    answer = 0
    empty_kola = n
    empty_kola_to_mart = lambda kola: (
        (kola // a) * b,
        kola % a,
    )

    while empty_kola >= a:
        empty_kola, empty_kola_2 = empty_kola_to_mart(empty_kola)
        answer += empty_kola
        empty_kola += empty_kola_2

    return answer


solution_v2 = lambda a, b, n: max(n - b, 0) // (a - b) * b

print(solution(2, 1, 20))
print(solution(3, 2, 20))
