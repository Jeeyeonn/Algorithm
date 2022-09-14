from collections import deque

n = int(input())

is_lion = []
for m in range(n):
    is_lion.append([0,0])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(q):
    while q:
        a,b = q.popleft()
        for i in range(4):
            a += dx[i]
            b += dy[i]
            if -1 < a < 2 and -1 < b <2 and is_lion[a][b] != 1:
                a = 0 #걍 쓴거임



qq = deque()
print(dfs(qq))