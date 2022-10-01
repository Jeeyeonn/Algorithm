def solution(k):
    num = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    num.sort(reverse= True)
    answer = []
    real_answer = 0
    for i in range(len(num)):
        ssum = num[i]
        if ssum > k:
            continue
        elif ssum == k:
            answer.append(1)
        else:
            result = str(num[i])
            for j in range(i, len(num)):
                if ssum+num[j] > k:
                    continue
                elif ssum+num[j] == k:
                    a = result
                    b = a.split("+")
                    answer.append(len(b)+1)
                else:
                    result += str(num[j])
                    ssum += num[j]


    for i in answer:
        numm = 1
        while i!=1:
            numm *= i
            i -= 1

        real_answer += numm

    return real_answer


solution(11) #99