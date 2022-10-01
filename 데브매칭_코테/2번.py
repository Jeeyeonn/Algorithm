from collections import deque


def solution(maps):
    answer = {}
    x = len(maps[0])
    y = len(maps)
    is_visited = []

    for _ in range(y):
        llist = []
        for _ in range(x):
            llist.append(False)
        is_visited.append(llist)

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if not is_visited[i][j] and maps[i][j] != '.':
                queue = deque()
                queue.append([i, j])
                is_visited[i][j] = True
                result = bfs(is_visited, queue, x, y, maps)
                for j in result:
                    value = result[j]
                    if j not in answer:
                        answer[j] = value
                    else:
                        answer[j] += value
    values = answer.values()

    return max(values)

def bfs(isvisited, q, x, y, map):
    num_list = {}

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        p = q.popleft()
        a = p[0]
        b = p[1]
        if map[a][b] in num_list:
            num_list[map[a][b]] += 1
        else:
            num_list[map[a][b]] = 1

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0<= nx < y and 0 <= ny < x:
                if isvisited[nx][ny] == False and map[nx][ny] != '.':
                    q.append([nx, ny])
                    isvisited[nx][ny] = True

    d1 = sorted(num_list.items(), key=lambda x: x[1], reverse=True)
    result = {}
    max_num = 0
    for i in d1:
        q = i
        if max_num == 0:
            max_num = q[1]
        if max_num == q[1]:
            # 문자 비교 ----------------------------------------------
            max_s = q[0]
            result[max_s] = max_num
        else:
            result[max_s] += q[1]
    return result

a = ["AABC..QA", "AABC..QX", "BBBC.Y..", ".A...T.A",
     "....EE..", ".M.XXEXQ", "KL.TBBBQ"]


b= ["XY..", "YX..", "..YX", ".AXY"]
print(solution(a))