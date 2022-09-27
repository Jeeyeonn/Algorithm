def solution(survey, choices):
    answer = ''
    sums = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for i in range(len(survey)):
        a, b = survey[i][0], survey[i][1]

        if choices[i] == 1:
            sums[a] += 3
        elif choices[i] == 2:
            sums[a] += 2
        elif choices[i] == 3:
            sums[a] += 1
        elif choices[i] == 5:
            sums[b] += 1
        elif choices[i] == 6:
            sums[b] += 2
        elif choices[i] == 7:
            sums[b] += 3

    if (sums["R"] >= sums["T"]):
        answer += "R"
    else:
        answer += "T"

    if (sums["C"] >= sums["F"]):
        answer += "C"
    else:
        answer += "F"

    if (sums["J"] >= sums["M"]):
        answer += "J"
    else:
        answer += "M"

    if (sums["A"] >= sums["N"]):
        answer += "A"
    else:
        answer += "N"

    return answer



a = ["AN", "CF", "MJ", "RT", "NA"]
b = [5, 3, 2, 7, 5]
c = ["TR", "RT", "TR"]
d = [7, 1, 3]

print(solution(c,d))