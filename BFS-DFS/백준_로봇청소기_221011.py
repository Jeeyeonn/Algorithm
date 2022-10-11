n, m = map(int, input().split())

x, y, dic = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited = [[False for _ in range(m)]for _ in range(n)]
visited[x][y] = True

answer = 1

while True:
    is_clean = False
    for i in range(4):
        nx = x + dx[(dic + 3) % 4]
        ny = y + dy[(dic + 3) % 4]
        dic = (dic + 3) % 4
        if 0<= nx < n and 0<= ny < m:
            if not visited[nx][ny] and map[nx][ny] != 1:
                visited[nx][ny] = True
                answer += 1
                is_clean = True
                x = nx
                y = ny
                break

    if not is_clean:  # 4방향 모두 청소가 되어 있을 때,
        if map[x - dx[dic]][y - dy[dic]] == 1:  # 후진했는데 벽
            print(answer)
            break
        else:
            x, y = x - dx[dic], y - dy[dic]