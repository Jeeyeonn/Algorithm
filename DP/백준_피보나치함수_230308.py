n = int(input())

dp = [[]for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]
c = 2

for _ in range(n):
    m = int(input())
    for i in range(c, m + 1):
        a = dp[i-1][0] + dp[i-2][0]
        b = dp[i-1][1] + dp[i-2][1]
        dp[i] = [a, b]
    print(str(dp[m][0]) + ' ' + str(dp[m][1]))
    c = max(c, m)