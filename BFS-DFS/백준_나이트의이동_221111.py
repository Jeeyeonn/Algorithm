from collections import deque

n = int(input())
isvisited = []

def bfs(queue, d_x, d_y):
    dx = [-1, -1, -2, -2, 1, 1, 2, 2]
    dy = [2, -2, 1, -1, 2, -2, 1, -1]

    while queue:
        x, y, cnt = queue.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < m and 0 <= ny < m and isvisited[nx][ny] == False:
                if nx == d_x and ny == d_y:
                    return cnt + 1
                queue.append([nx, ny, cnt + 1])
                isvisited[nx][ny] = True

for i in range(n):
    m = int(input())
    c_x, c_y = list(map(int, input().split()))
    d_x, d_y = list(map(int, input().split()))
    isvisited = [[False for _ in range(m)] for _ in range(m)]
    if c_x == d_x and c_y == d_y:
        print(0)
    else:
        q = deque()
        q.append([c_x, c_y, 0])
        print(bfs(q, d_x, d_y))


