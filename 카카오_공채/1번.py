def solution(today, terms, privacies):
    answer = []

    today_list = today.split(".")
    today_Y = int(today_list[0])
    today_M = int(today_list[1])
    today_D = int(today_list[2])

    for i in range(len(privacies)):
        p_dayy = privacies[i].split(" ")
        p_day = p_dayy[0].split(".")
        p_y = int(p_day[0])
        p_m = int(p_day[1])
        p_d = int(p_day[2])
        p_a = p_dayy[1]

        trem = 0
        for n in terms:
            if p_a == n[:1]:
                trem = n[1:]
                break
        p_m += int(trem)
        while p_m > 12:
            p_y += 1
            p_m -= 12
        p_d -= 1
        if p_d == 0:
            p_d = 28
            p_m -= 1
            if p_m == 0:
                p_m = 12
                p_y -= 1


        if p_y < today_Y:
            answer.append(i+1)
        elif p_y == today_Y:
            if p_m < today_M:
                answer.append(i+1)
            elif p_m == today_M:
                if p_d < today_D:
                    answer.append(i+1)

    print(answer)

    return answer

a = "2022.05.19"
b = ["A6", "B12", "C3"]
c = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

solution(a,b,c)