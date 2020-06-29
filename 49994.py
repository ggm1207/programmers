def solution(dirs):
    # arrived pos and prev order
    y, x = 0, 0
    pos = dict()
    move = {'U':(1, 0), 'L':(0, -1), 'R':(0, 1), 'D':(-1, 0)}
    for d in dirs:
        ny, nx = y + move[d][0], x + move[d][1]
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            key = tuple(sorted([(y, x), (ny, nx)]))
            y, x = ny, nx
            pos[key] = True
    return len(pos)

if __name__ == "__main__":
    t_case = []
    t_case.append(["ULURRDLLU"]) # return 7
    t_case.append(["LULLLLLLU"]) # return 7

    for tc in t_case:
        print(solution(*tc))
