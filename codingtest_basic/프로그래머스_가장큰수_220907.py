from itertools import permutations


def solution(numbers):
    answer = []

    for i in numbers:
        answer.append(str(i))

    answer.sort(reverse=True)
    print(answer)

    for j in range(len(answer)-1):
        a = list(answer[j])
        b = list(answer[j+1])
        if a[0] == b[0]:
            if len(a) > len(b):
                temp = answer[j]
                answer[j] = answer[j+1]
                answer[j+1] = temp

    return ''.join(answer)

def solution2(numbers):
    answer = 0

    num_list = list(permutations(numbers, len(numbers)))
    for i in num_list:
        num = ''
        for j in i:
            num += str(j)
        answer = max(answer, int(num))

    return answer


a = [212, 21, 211]
print(solution2(a))