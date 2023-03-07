def solution(fees, records):
    answer = []
    for i in range(len(records)):
        records[i] = records[i].split(" ")
    records = sorted(records, key=lambda records: records[1])
    cnt_car = records[0][1]
    hour, minute = 0, 0
    sum_min = 0
    is_car = True

    for i in range(len(records)):
        if cnt_car == records[i][1]:
            if is_car:
                hour = int(records[i][0].split(":")[0])
                minute = int(records[i][0].split(":")[1])
                is_car = False
            else:
                sum_min += (
                    (int(records[i][0].split(":")[0]) - hour) * 60
                    + int(records[i][0].split(":")[1])
                    - minute
                )
                hour, minute = 0, 0
                is_car = True
        else:
            if is_car:
                hour = int(records[i][0].split(":")[0])
                minute = int(records[i][0].split(":")[1])
                cnt_car = records[i][1]
                answer.append(sum_min)
                sum_min = 0
                is_car = False
            else:
                sum_min += (23 - hour) * 60 + 59 - minute
                answer.append(sum_min)
                hour = int(records[i][0].split(":")[0])
                minute = int(records[i][0].split(":")[1])
                cnt_car = records[i][1]
                sum_min = 0
                is_car = False
        if i == len(records) - 1:
            if not is_car:
                sum_min += (23 - hour) * 60 + 59 - minute
                answer.append(sum_min)
            else:
                answer.append(sum_min)

    for j in range(len(answer)):
        if answer[j] > fees[0]:
            if (answer[j] - fees[0]) % fees[2] == 0:
                remain_min = (answer[j] - fees[0]) // fees[2]
            else:
                remain_min = (answer[j] - fees[0]) // fees[2] + 1
            answer[j] = fees[1] + remain_min * fees[3]
        else:
            answer[j] = fees[1]

    return answer


print(solution([1, 10, 1, 11], ["00:00 1234 IN", "00:02 1234 OUT"]))
print(
    solution(
        [180, 5000, 10, 600],
        [
            "05:34 5961 IN",
            "06:00 0000 IN",
            "06:34 0000 OUT",
            "07:59 5961 OUT",
            "07:59 0148 IN",
            "18:59 0000 IN",
            "19:09 0148 OUT",
            "22:59 5961 IN",
            "23:00 5961 OUT",
        ],
    )
)
print(
    solution(
        [120, 0, 60, 591],
        [
            "16:00 3961 IN",
            "16:00 0202 IN",
            "18:00 3961 OUT",
            "18:00 0202 OUT",
            "23:58 3961 IN",
        ],
    )
)
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
