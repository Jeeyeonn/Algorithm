n = int(input())

for _ in range(n):
    m = int(input())
    item_cnt = {}
    item = []
    cnt = 1
    for _ in range(m):
        a, b = input().split()
        if b in item_cnt:
            item_cnt[b] += 1
        else:
            item_cnt[b] = 1
            item.append(b)
    for ii in item:
        cnt *= item_cnt[ii] + 1
    print(cnt - 1)