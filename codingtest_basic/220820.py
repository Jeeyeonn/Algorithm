# 백준 11048 : 이동하기

n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))

dx = [1, 0, 1]
dy = [0, 1 ,1]

def soultion(a,b):
    num = 0
    num += s[a][b]
    for i in range(3):
        a += dx[i]
        b += dy[i]
        if 0 < a and a < n and b >0 and b < m:
            num += soultion(a,b)

    return num

print(soultion(0,0))