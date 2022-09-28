n, m = map(int, input().split(" "))
inputs = []
interval = []

for i in range(n):
    a = int(input())
    inputs.append(a)

inputs.sort()

for i in range(1, n):
    interval.append(abs(inputs[i] - inputs[i - 1]))

num = (inputs[0]+inputs[len(inputs)-1]-2)//(m-1)

ssum = interval[0]
count = 1
answer = []


for i in range(1, len(interval)):
    if abs(num - ssum) > abs(num - ssum - interval[i]):
        ssum += interval[i]
        if i == len(interval)-1:
            answer.append(ssum)
    else:
        if count != m:
            count += 1
            answer.append(ssum)
            ssum = interval[i]
        else:
            if i == len(interval) - 1:
                answer.append(ssum)
            else:
                ssum += interval[i]

print(answer)
print(min(answer))
