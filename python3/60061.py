class BAR:
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y
        self.name = 0

    def checking(self, maps: dict):
        if self.y == 0:
            return True

        try:
            if maps[self.x, self.y - 1, 0].name == 0:
                return True
        except:
            pass

        try:
            if maps[self.x - 1, self.y, 1].name == 1:
                return True
        except:
            pass

        try:
            if maps[self.x, self.y, 1].name == 1:
                return True
        except:
            pass

        return False


class FLOOR:
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y
        self.rx = x + 1
        self.ry = y
        self.name = 1

    def checking(self, maps: dict):
        try:
            if maps[self.x, self.y - 1, 0].name == 0:
                return True
        except:
            pass
        try:
            if maps[self.rx, self.ry - 1, 0].name == 0:
                return True
        except:
            pass
        try:
            if (maps[self.x - 1, self.y, 1].name == 1) and (
                maps[self.rx, self.ry, 1].name == 1
            ):
                return True
        except:
            pass

        return False


def solution(n, build_frame):
    maps = dict()

    for x, y, structure, install in build_frame:
        if structure == 1:  # FLOOR
            obj = FLOOR(n, x, y)
        else:
            obj = BAR(n, x, y)

        if install == 1:
            if not obj.checking(maps):
                continue
            maps[x, y, structure] = obj
        else:  # delete
            flag = True

            temp = maps.pop((x, y, structure))

            for v in maps.values():
                flag = flag and v.checking(maps)

            if not flag:
                maps[x, y, structure] = temp

    answer = [[k[0], k[1], k[2]] for k in maps.keys()]
    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer


if __name__ == "__main__":
    t_case = []
    t_case.append(
        [
            5,
            [
                [1, 0, 0, 1],
                [1, 1, 1, 1],
                [2, 1, 0, 1],
                [2, 2, 1, 1],
                [5, 0, 0, 1],
                [5, 1, 0, 1],
                [4, 2, 1, 1],
                [3, 2, 1, 1],
            ],
        ]
    )  # return [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
    t_case.append(
        [
            5,
            [
                [0, 0, 0, 1],
                [2, 0, 0, 1],
                [4, 0, 0, 1],
                [0, 1, 1, 1],
                [1, 1, 1, 1],
                [2, 1, 1, 1],
                [3, 1, 1, 1],
                [2, 0, 0, 0],
                [1, 1, 1, 0],
                [2, 2, 0, 1],
            ],
        ]
    )  # return [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

    for tc in t_case:
        print(solution(*tc))
