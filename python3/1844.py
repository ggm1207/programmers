def solution(maps):
    n, m = len(maps), len(maps[0])
    last_point = (n-1, m-1) 
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
   
    def check(y, x):
        if (0 <= y < n) & (0 <= x < m):
            return maps[y][x]
        return 0
    
    queue = [(0, 0, 0)]
    while(queue):
        cy, cx, cnt = queue[0]
        if (cy, cx) == last_point:
            return cnt + 1

        for my, mx in move:
            ny, nx = my + cy, mx + cx
            if check(ny, nx):
                queue.append((ny, nx, cnt+1))
                maps[ny][nx] = 0  

        queue = queue[1:]
        
    return -1        

if __name__ == "__main__":
    t_case = []
    t_case.append([[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]])
    t_case.append([[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]])
    for tc in t_case: 
        print(solution(*tc))
