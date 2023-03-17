n, k = list(map(int, input().split()))
price = []
for _ in range(n):
    price.append(int(input()))
cnt = 0

for i in range(len(price)-1, -1, -1):
    if k >= price[i]:
        cnt += k // price[i]
        k = k - (price[i] * (k//price[i]))
print(cnt)