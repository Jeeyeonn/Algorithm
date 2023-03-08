import sys
from collections import deque
input = sys.stdin.readline

n, m = list(map(int, input().split()))
graph = [list(input())[:-1] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dis = [[0 for _ in range(m)] for _ in range(n)]
answer = 0
q = deque()
q.append([0, 0, 0, visited])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y, count, vis = q.popleft()
    vis[x][y] = True
    if dis[x][y] != 0 and dis[x][y] < count:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0<= ny < m:
            if not vis[nx][ny] and graph[nx][ny] == '1':
                if dis[nx][ny] == 0 or dis[nx][ny] > count + 1:
                    dis[nx][ny] = count + 1
                    q.append([nx, ny, count + 1, vis])
print(dis[n-1][m-1]+1)