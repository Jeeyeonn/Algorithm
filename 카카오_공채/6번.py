from collections import deque


def solution(m, n, y, x, c, r, k):

    result = []
    a = [x, y, 0, '']
    q = deque([a])

    dx = [0, 0, 1, -1]  #u, d, r, l
    dy = [1, -1, 0, 0]

    while q:
        p = q.popleft()
        x, y, d, h = p[0], p[1], p[2], p[3]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = d + 1
            if i == 0:
                nh = h + 'd'
            elif i == 1:
                nh = h + 'u'
            elif i == 2:
                nh = h + 'r'
            else:
                nh = h + 'l'

            if 0< nx <= n and 0< ny <= m:
                if nd > k:
                    break
                if nx == r and ny == c and nd == k:
                    result.append(nh)
                else:
                    if nd != k:
                        q.append([nx, ny, nd, nh])

    result.sort()
    if len(result) != 0:
        return result[0]
    else:
        return 'impossible'



print(solution(3, 4, 2, 3, 3, 1, 5))   #dllrl
#print(solution(2, 2, 1, 1, 2, 2, 2))
#print(solution(3, 3, 1, 2, 3, 3, 4))
