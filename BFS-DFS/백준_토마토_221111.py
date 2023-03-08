from collections import deque

n, m = list(map(int, input().split()))
tomato = [list(map(int, input().split())) for _ in range(m)]

def bfs(a, b):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append([a, b])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0<= ny < n and tomato[nx][ny] != -1:
                if tomato[nx][ny] != 0:
                    if tomato[nx][ny] > tomato[x][y] + 1:
                        tomato[nx][ny] = tomato[x][y] + 1
                        q.append([nx, ny])
                else:
                    tomato[nx][ny] = tomato[x][y] + 1
                    q.append([nx, ny])

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            bfs(i, j)

cnt = 0
day = 0
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 0:
            cnt += 1
    day = max(day, max(tomato[i]))

if cnt == 0:
    print(day-1)
else:
    print(-1)