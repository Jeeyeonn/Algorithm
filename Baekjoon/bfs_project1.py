# 백준 2606번 : 바이러스
# 너비 우선탐색

from collections import deque

N = int(input())
M = int(input())
bb = [[int(x) for x in input().split()]for y in range(M)]
is_visited = [False] * (N+1)

def solution(c):
    queue = deque([1])
    is_visited[1] = True

    while queue:
        v = queue.popleft()

        for i in range(M):
            if c[i][0] == v:
                if not is_visited[c[i][1]]:
                    is_visited[c[i][1]] = True
                    queue.append(c[i][1])
            elif c[i][1] == v:
                if not is_visited[c[i][0]]:
                    is_visited[c[i][0]] = True
                    queue.append(c[i][0])

answer = 0
solution(bb)
for a in range(len(is_visited)):
    if is_visited[a]:
        answer += 1

print(answer - 1)
