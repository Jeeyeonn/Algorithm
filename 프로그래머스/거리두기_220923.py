from collections import deque


def solution(places):
    answer = []

    for i in places:
        answer.append(bfs(i))
    return answer

def bfs(i):
    p_point = []

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for a in range(5):
        for b in range(5):
            if i[a][b] == 'P':
                p_point.append([a, b, 0])


    for c in p_point:
        q = deque([c])
        is_visited = [[False]*5 for _ in range(5)]

        while q:
            p = q.popleft()
            x, y, d = p[0], p[1], p[2]
            is_visited[x][y] = True

            if 0 < d and i[x][y] == 'P':
                return 0

            if d == 1 or d == 0:

                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]
                    nd = d + 1

                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if is_visited[nx][ny] != True:
                            if i[nx][ny] != 'X':
                                is_visited[nx][ny] = True
                                q.append([nx, ny, nd])
                            elif i[nx][ny] == 'P':
                                return 0

    return 1







a = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
     ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
     ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

b = 	[["POOOP", "OXXOX", "OXXPX", "OPXOX", "PXXXP"],
        ["POOOP", "OXXOX", "OXXPX", "OPXOX", "PXXXP"],
        ["POOOP", "OXXOX", "OXXPX", "OPXOX", "PXXXP"],
        ["POOOP", "OXXOX", "OXXPX", "OPXOX", "PXXXP"],
        ["POOOP", "OXXOX", "OXXPX", "OPXOX", "PXXXP"]]

print(solution(b))