"""순위 검색
중요
    - 4가지 항목 선택
    - 지원 조건 선택, 필터링
    - 조건이 1 ~ 4개 사이로 들어옴.
        - [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?
인사이트
    - 
"""


def solution(info, query):
    answer = []

    for q in query:
        condition = q.split(" ")
        condition = condition[::2] + [condition[-1]]
        res = 0

        for inf in info:
            for idx, (i, c) in enumerate(zip(inf.split(), condition)):
                if idx == 4 and int(i) < int(c):
                    break
                elif idx != 4 and i != c and c != "-":
                    break
            else:
                res += 1

        answer.append(res)

    return answer


info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50",
]
query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150",
]

print(solution(info, query))
