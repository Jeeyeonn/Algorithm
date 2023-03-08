# 백준 16930

import sys
from collections import deque

input = sys.stdin.readline

n, m, k = list(map(int, input().split()))
gym = [list(input())[:-1] for _ in range(n)]
x1, y1, x2, y2 = list(map(int, input().split()))

q = deque()
visited = [[False for _ in range(m)] for _ in range(n)]
distinse = [[0 for _ in range(m)] for _ in range(n)]
answer = -1
nx = [1, -1, 0, 0]
ny = [0, 0, 1, -1]

for i in range(4):
    if 0<= x1 + nx[i] -1 < n and 0<= y1 + ny[i] -1 < m:
        if gym[x1 + nx[i] -1][y1 + ny[i] -1] == '.':
            q.append([x1-1, y1-1, i, 1, 0, visited])

while q:
    a, b, dir, dis, total_dis, vis = q.popleft()
    if answer != -1 and answer < total_dis:
        continue
    vis[a][b] = True
    for i in range(4):
        x = a + nx[i]
        y = b + ny[i]
        if 0<= x < n and 0<= y < m:
            if not vis[x][y] and gym[x][y] == '.':
                if i == dir:
                    if distinse[x][y] == 0 or (distinse[x][y] != 0 and total_dis <= distinse[x][y]):
                        if dis == k:
                            distinse[x][y] = total_dis + 1
                            q.append([x, y, dir, 1, total_dis + 1, vis])
                        else:
                            if total_dis == 0:
                                total_dis += 1
                            q.append([x, y, dir, dis + 1, total_dis, vis])
                            distinse[x][y] = total_dis
                else:
                    if distinse[x][y] == 0 or (distinse[x][y] != 0 and total_dis <= distinse[x][y]):
                        q.append([x, y, i, 1, total_dis +1, vis])
                        distinse[x][y] = total_dis + 1
if distinse[x2-1][y2-1] == 0:
    print(-1)
else:
    print(distinse[x2-1][y2-1])
            