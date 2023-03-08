import sys
from collections import deque
input = sys.stdin.readline
 
n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int, input().split())))

white, blue = 0, 0

def fun(size, color, graph):
    global white, blue
    result = True
    for i in range(size):
        if graph[i].count(color) != size:
            result = False
            break
    if not result:
        for j in range(0, size, size//2):
            for k in range(0, size, size//2):
                g = []
                for l in range(j, j + size//2):
                    g.append(graph[l][k : k + size//2])
                fun(size//2, graph[j][k], g)
    else:
        if color == 0:
            white += 1
        else:
            blue += 1
fun(n, g[0][0], g)
print(white)
print(blue)