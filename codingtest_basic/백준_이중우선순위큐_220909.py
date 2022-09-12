n = int(input())
answer= []

for _ in range(n):
    m = int(input())
    for _ in range(m):
        inputs = input()
        sign = inputs.split()[0]
        num = int(inputs.split()[1])

        if sign == 'I':
            answer.append(num)
        else:
            if num == 1:
                if len(answer) != 0:
                    max_num = max(answer)
                    index = answer.index(max_num)
                    del answer[index]
            else:
                if len(answer) != 0:
                    min_num = min(answer)
                    index = answer.index(min_num)
                    del answer[index]
    if len(answer) != 0:
        print(max(answer), min(answer))
    else:
        print("EMPTY")