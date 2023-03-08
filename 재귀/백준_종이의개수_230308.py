import sys
from collections import deque
input = sys.stdin.readline
 
nn = int(input())
g = []
for _ in range(nn):
    g.append(list(map(int, input().split())))
cnt = g[0][0]


a, b, c = 0, 0, 0

def fun(n, num, graph):
    global a, b, c
    result = True
    for i in range(n):
        if graph[i].count(num) != n:
            result = False

    if not result:
        for j in range(0, n, n//3):
            for k in range(0, n, n//3):
                g = []
                for l in range(j, j+n//3):
                    g.append(graph[l][k : k + n//3])
                fun(n//3, graph[j][k], g)
    else:
        if num == -1:
            a += 1
        elif num == 0:
            b += 1
        elif num == 1:
            c += 1

fun(nn, cnt, g)
print(a)
print(b)
print(c)

