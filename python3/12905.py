def solution(board):
    w, h = len(board[0]), len(board)
    _max = 0

    if w + h < 4:
        _max = max([max(b) for b in board])

    for _w in range(1, w):
        for _h in range(1, h):
            checks = [board[_h - y][_w - x] for y, x in [(1, 0), (0, 1), (1, 1)]]
            _min = min(checks)

            board[_h][_w] = _min + 1 if board[_h][_w] else 0
            _max = max(_max, board[_h][_w])

    return _max * _max



if __name__ == "__main__":
    t_case = []
    t_case.append([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])
    t_case.append([[0,0,1,1],[1,1,1,1]])
    t_case.append([[0]])
    t_case.append([[0, 1], [1, 1]])
    t_case.append([[0, 1]])

    for tc in t_case:
        print(solution(tc))
