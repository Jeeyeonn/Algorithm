n = int(input())
times = list(map(int, input().split()))
times.sort()
sum_time = 0
for time in times:
    sum_time += time * n
    n -= 1
print(sum_time)