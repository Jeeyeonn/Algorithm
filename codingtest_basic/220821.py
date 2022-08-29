# 백준 2468 : 안전영역

# 일단 1부터 max넘까지 돈다. -> height
# 하나씩 칠한다.
# 최대를 구한다.

from collections import deque

#입력값
n = int(input())
graph = []
maxNum = 0


for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j]



dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def bfs(a,b,h, visited):
    queue = deque()
    queue.append((a, b))

    visited[a][b] = 1

    while queue:
        a,b = queue.popleft()
        for i in range(4):
            aa = a + dx[i]
            bb = b + dy[i]
            if 0 <= aa < n and 0 <= bb < n:
                if visited[aa][bb]==0 and graph[aa][bb] > h:
                    visited[aa][bb] = 1
                    queue.append((aa,bb))

answer = 0

for j in range(1, maxNum):
    is_visited = [[0] * n for i in range(n)]
    count = 0
    for q in range(n):
        for w in range(n):
            if is_visited[q][w] == 0 and graph[q][w] > j:
                bfs(q, w, j, is_visited)
                count += 1

    answer = max(count, answer)

print(answer)