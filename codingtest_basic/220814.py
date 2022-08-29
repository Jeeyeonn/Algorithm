# 백준 12865: 평범한 배낭

JS = list(map(int, input().split()))
things = [[int(x) for x in input().split()]for y in range(JS[0])]

things.sort()
things.reverse()

value = 0

for a in range(len(things)):

    for b in range(a+1, len(things)):
        value_2 = things[a][1]
        if things[a][0] + things[b][0] <= JS[1]:

            value_2 += things[b][1]
            sum = things[a][0] + things[b][0]
            temp = b+1

            while temp < len(things) and sum < JS[1]:
                if sum + things[temp][0] <= JS[1]:
                    value_2 += things[temp][1]
                temp += 1

        value = max(value, value_2)
    value = max(value, value_2)


print(value)