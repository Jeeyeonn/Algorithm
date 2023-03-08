n, m = list(map(int, input().split()))
name = {}
r = []
for i in range(n+m):
    if i < n:
        name[input()] = 1
    else:
        nn = input()
        if nn in name:
            r.append(nn)
r.sort()
print(len(r))
for rr in r:
    print(rr)