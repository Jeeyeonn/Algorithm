n = int(input())
inputs = []
for i in range(n):
    inputs.append(list(map(int, input().split())))

answer = []
answer.append(inputs[0])

for j in range(1, len(inputs)):
    num_list = []
    for k in range(len(inputs[j])):
        if k==0:
            num_list.append(answer[j-1][0] + inputs[j][k])
        elif k == len(inputs[j])-1:
            num_list.append(answer[j - 1][k-1] + inputs[j][k])
        else:
            max_num = max(answer[j-1][k-1], answer[j-1][k])
            num_list.append(inputs[j][k]+max_num)
    answer.append(num_list)

print(max(answer[len(answer)-1]))