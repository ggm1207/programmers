import re


def solution(user_id, banned_id):
    bann_len = len(banned_id)
    bann_set = set()

    def user_to_re(user):
        return "".join(list(map(lambda x: "[%s]" % x if x != "*" else ".", user)))

    def dfs(user_id, banned_id, sol, depth):
        if len(sol) == bann_len:
            bann_set.add("".join(sorted(sol)))
            return

        bann = banned_id[depth]
        banners = re.findall(
            user_to_re(bann), "\n".join(filter(lambda x: len(x) == len(bann), user_id))
        )

        for banner in banners:
            user_id.pop(user_id.index(banner))
            dfs(user_id, banned_id, sol[:] + [banner], depth + 1)
            user_id.append(banner)

    dfs(user_id, banned_id, [], 0)
    return len(bann_set)


if __name__ == "__main__":
    t_case = []
    t_case.append(
        [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]]
    )  # return 2
    t_case.append(
        [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]]
    )  # return 2
    t_case.append(
        [
            ["frodo", "fradi", "crodo", "abc123", "frodoc"],
            ["fr*d*", "*rodo", "******", "******"],
        ]
    )  # return 3

    for tc in t_case:
        print(solution(*tc))
