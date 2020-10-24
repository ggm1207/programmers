# Make traffic: means tuple of (start_log, end_log)
# Make


def solution(lines):
    answer, len_lines, count = 1, len(lines), 1
    start, finish = [], []

    for log in lines:
        tmp = float(log[11:13]) * 3600 + float(log[14:16]) * 60 + float(log[17:23])
        finish.append(tmp)
        start.append(round(tmp - float(log[24:-1]) + 0.001, 3))

    for i in range(len_lines):
        count = 1
        for j in range(i + 1, len_lines):
            if finish[i] + 1 > start[j]:
                count += 1
        answer = max(answer, count)

    return answer


print(solution(["2016-09-15 00:00:00.000 3s"]))
print(solution(["2016-09-15 23:59:59.999 0.001s"]))
print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(
    solution(
        [
            "2016-09-15 20:59:57.421 0.351s",
            "2016-09-15 20:59:58.233 1.181s",
            "2016-09-15 20:59:58.299 0.8s",
            "2016-09-15 20:59:58.688 1.041s",
            "2016-09-15 20:59:59.591 1.412s",
            "2016-09-15 21:00:00.464 1.466s",
            "2016-09-15 21:00:00.741 1.581s",
            "2016-09-15 21:00:00.748 2.31s",
            "2016-09-15 21:00:00.966 0.381s",
            "2016-09-15 21:00:02.066 2.62s",
        ]
    )
)
print(solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]))
