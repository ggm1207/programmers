from collections import defaultdict


def solution(gems):
    gems_len = len(set(gems))
    gems_last_idx = defaultdict(int)

    answer = []

    for idx, gem in enumerate(gems):
        gems_last_idx[gem] = idx + 1

        if len(gems_last_idx) == gems_len:
            gems_name, last_idx = zip(*gems_last_idx.items())
            min_idx, max_idx = min(last_idx), max(last_idx)
            answer.append([min_idx, max_idx])
            del gems_last_idx[gems_name[last_idx.index(min_idx)]]

    answer = sorted(answer, key=lambda x: (x[1] - x[0], x[0]))

    return answer[0]


if __name__ == "__main__":
    t_case = []
    t_case.append(
        [["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]]
    )  # return [3, 7]
    t_case.append([["AA", "AB", "AC", "AA", "AC"]])  # return [1, 3]
    t_case.append([["XYZ", "XYZ", "XYZ"]])  # return [1, 1]
    t_case.append([["ZZZ", "YYY", "NNNN", "YYY", "BBB"]])  # return [1, 5]
    t_case.append([["A", "B", "C", "A", "C"]])  # return [1, 3]
    t_case.append(
        [["B", "B", "A", "A", "C", "A", "A", "C", "B"]]
    )  # return [1, 3]
    # t_case.append([["B", "B", "A"]]) # return [1, 3]
    # t_case.append([["A"]]) # return [1, 3]

    for tc in t_case:
        print(solution(*tc))
