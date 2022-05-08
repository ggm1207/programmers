from collections import defaultdict


def solution(id_list, report, k):
    report_list, report_cnt = defaultdict(list), defaultdict(int)
    visited = set()

    for r in report:
        f_id, t_id = r.split()
        if r in visited:
            continue

        report_list[f_id].append(t_id)
        report_cnt[t_id] += 1
        visited.add(r)

    answer = []

    for f_id in id_list:
        mail_cnt = sum([report_cnt[r_id] >= k for r_id in report_list[f_id]])
        answer.append(mail_cnt)

    return answer


print(
    solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2,
    )
)

print(
    solution(
        ["con", "ryan"],
        ["ryan con", "ryan con", "ryan con", "ryan con"],
        3,
    )
)
