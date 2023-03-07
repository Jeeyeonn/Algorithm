import sys
from collections import deque
input = sys.stdin.readline

n, m, k = list(map(int, input().split()))
map_list = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
answer = 0
for _ in range(k):
    x, y = list(map(int, input().split()))
    map_list[x-1][y-1] = 1

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    q = deque()
    q.append([x, y])

    while q:
        a, b = q.popleft()
        if not visited[a][b]:
            visited[a][b] = True
            cnt += 1
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<= nx < n and 0<= ny < n:
                    if visited[nx][ny] == False and map_list[nx][ny] == 1:
                        q.append([nx, ny])
    return cnt

for x in range(n):
    for y in range(m):
        if visited[x][y] == False and map_list[x][y] == 1:
            num = bfs(x, y)
            answer = max(answer, num)
print(answer)