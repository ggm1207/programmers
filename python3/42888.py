def solution(record):
    answer = []
    uid = dict()
    for log in record:
        logsplit = log.split(" ")
        if logsplit[0] == "Enter":
            answer.append(("{}님이 들어왔습니다.", logsplit[1]))
            uid[logsplit[1]] = logsplit[2]
        elif logsplit[0] == "Leave":
            answer.append(("{}님이 나갔습니다.", logsplit[1]))
        else:
            uid[logsplit[1]] = logsplit[2]
    return list(map(lambda x: x[0].format(uid[x[1]]), answer))

if __name__ == "__main__":
    t_case = []
    t_case.append(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

    for tc in t_case:
        print(solution(tc))
