def solution(numbers):
    answer = []

    for i in numbers:
        ok = True
        result = two(i)
        if result == '-1':
            answer.append(0)
        else:
            result_list = []
            result_list.append(result)
            num = []
            middle = 0
            while True:
                for j in result_list:
                    middle = len(j) // 2
                    if j[middle] == '0':
                        ok = False
                        break
                    num.append(j[:middle])
                    num.append(j[middle+1:])

                result_list = num
                num = []
                if middle == 1:
                    break
            if ok:
                answer.append(1)
            else:
                answer.append(0)

    return answer

def solution2(numbers):
    answer = []

    for i in numbers:
        ok = True
        result = two(i)
        j = 1

        if result == '3':
            answer.append(0)

        else:

            while j < len(result):
                if result[j] == '0':
                    ok = False
                    break
                else:
                    j += 2

            if ok:
                answer.append(1)
            else:
                answer.append(0)

    return answer


def two(a):
    answer = ''
    #bin(a)
    while True:
        if a == 0:
            break
        else:
            answer += str(a % 2)
            a = a//2

    #  0 0 1 1 111          
    if len(answer) % 2 == 0:
        if (len(answer)//2) % 2 == 0:
            answer = '3'
        else:
            answer += '0'
    else:
        if (len(answer)//2) % 2 == 0:
            answer = '3'

    answer = answer[::-1]
    return answer

a = [31, 5]
b = [63, 111, 95]
c = [10]
print(solution2(c))