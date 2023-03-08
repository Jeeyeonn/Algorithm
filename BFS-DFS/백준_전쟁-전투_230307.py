import sys
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().split()))
map_list = [list(input())[:-1] for _ in range(m)]
w, b = 0, 0
visited = [[False for _ in range(n)] for _ in range(m)]

def bfs(word, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    q = deque()
    q.append([word, x, y])

    while q:
        w, a, b = q.popleft()
        if not visited[a][b]:
            visited[a][b] = True
            cnt += 1
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<= nx < m and 0<= ny < n:
                    if visited[nx][ny] == False and map_list[nx][ny] == w:
                        q.append([w, nx, ny])
    return cnt

for x in range(m):
    for y in range(n):
        if visited[x][y] == False:
            num = bfs(map_list[x][y], x, y)
            if map_list[x][y] == 'W':
                w += num * num
            else:
                b += num * num
print(w, b)

