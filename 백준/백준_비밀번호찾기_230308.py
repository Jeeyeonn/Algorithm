n, m = list(map(int, input().split()))
save = {}
for idx in range(n+m):
    if idx < n:
        site, pw = input().split()
        save[site] = pw
    else:
        site = input()
        print(save[site])