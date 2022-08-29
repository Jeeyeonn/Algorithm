# 백준 2667번 : 단지 번호 붙이기

from collections import deque

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

def bfs(a, b):
    count = 0
    one = 0
    two = 0
    three = 0
    four = 0
    if graph[a][b] == 1:
        count += 1
        graph[a][b] = 0
        if a != 0:
            one = bfs(a-1, b)
        if a != N-1:
            two = bfs(a+1, b)
        if b != N-1:
            three = bfs(a, b+1)
        if b != 0:
            four = bfs(a, b-1)

    return count +one+two+three+four

answer = []
for c in range(N):
    for d in range(N):
        if graph[c][d] != 0:
            answer.append(bfs(c, d))

answer.sort()

print(len(answer))
for i in answer:
    print(i)