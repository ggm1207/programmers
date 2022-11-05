"""
    - 조리된 순서대로 상수의 앞에 아래서부터 위로 쌓인다.
    - 빵(1), 야채(2), 고기(3), 빵(1)

    메모
        - index는 천천히 접근해야 한다. (주석 표시)
        - 리스트 요소를 제거할 때는 del 사용해서 제거
        - 시간 초과 났던 이유
            - 리스트 요소를 제거하기 위해 요소가 제거된
            - 새로운 리스트 만드는 연산을 계속해서 사용
"""


def solution(ingredient):
    answer = 0
    hamburger = [1, 2, 3, 1]
    i = 0

    while i < len(ingredient) - 3:  # 인덱스
        if hamburger == ingredient[i : i + 4]:
            answer += 1

            for _ in range(4):
                del ingredient[i]

            i -= 2  # 인덱스
            continue

        i += 1

    return answer


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
