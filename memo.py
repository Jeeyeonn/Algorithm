n, r, c = list(map(int, input().split()))
answer = 0

for i in range(n, 0, -1):
    cnt = 2 ** i
    if r < cnt //2 and c < cnt // 2:
        continue
    elif r >= cnt // 2 and c < cnt // 2:
        answer += (cnt**2) // 2
        r -= cnt // 2
    elif r < cnt // 2 and c >= cnt // 2:
        answer += (cnt**2) // 4
        c -= cnt // 2
    else:
        answer += (cnt**2) // 4 * 3
        r -= cnt // 2
        c -= cnt // 2
print(answer)