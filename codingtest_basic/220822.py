# 백준 16234 : 인구이동

from collections import deque
import sys

#입력값
n, mmin, mmax = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))


dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

queue2 = deque()  #데크

def bfs(a, b, visited):
    queue = deque()
    queue.append((a, b))
    sum = 0


    visited[a][b] = 1

    while queue:
        a,b = queue.popleft()
        for i in range(4):
            aa = a + dx[i]
            bb = b + dy[i]
            if 0 <= aa < n and 0 <= bb < n:
                if visited[aa][bb] == 0 and mmin <= abs(graph[aa][bb] - graph[a][b]) <= mmax:
                    visited[aa][bb] = 1
                    queue.append((aa, bb))
                    queue2.append((aa, bb))
                    sum += graph[aa][bb]
    return sum


answer = 0

while True:
    is_visited = [[0] * n for i in range(n)]
    queue2.clear()
    count = 0

    for q in range(n):
        for w in range(n):
            if is_visited[q][w] == 0:
                sum = bfs(q, w, is_visited)

                if queue2:
                    queue2.appendleft((q, w))
                    sum += graph[q][w]
                    size = len(queue2)
                    count = 1
                    while queue2:
                        i, j = queue2.popleft()
                        graph[i][j] = sum // size
    if count == 0:
        break
    else:
        answer += 1


print(answer)