
def goto_SUN(a):
    b = 0
    if a == "MON":
        b = 6
    elif a == "TUE":
        b = 5
    elif a == "WED":
        b = 4
    elif a == "THU":
        b = 3
    elif a == "FRI":
        b = 2
    elif a == "SAT":
        b = 1

    return b


def goto_SAT(a):
    b = 0
    if a == "MON":
        b = 5
    elif a == "TUE":
        b = 4
    elif a == "WED":
        b = 3
    elif a == "THU":
        b = 2
    elif a == "FRI":
        b = 1
    elif a == "SUN":
        b = 6

    return b



def solution(join_date, resign_date, holidays):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days2 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    j_list = ["0"] * 4
    j_list[0] = join_date.split("/")[0]
    j_list[1] = join_date.split("/")[1]
    cut = join_date.split("/")[2]
    j_list[2] = cut.split(" ")[0]
    j_list[3] = cut.split(" ")[1]

    #j_list2 = []
    #dayss, date = join_date.split()
    #year, month, dayy = dayss.split("/")
    #j_list2.append([year,month,dayy,date])

    # ["2019",12,01,MON]

    r_list = ["0"] * 3
    r_list[0] = resign_date.split("/")[0]
    r_list[1] = resign_date.split("/")[1]
    r_list[2] = resign_date.split("/")[2]

    answer = []

    # 전체 일 수 구하기
    j_year = int(j_list[0])
    j_month = int(j_list[1])
    j_day = int(j_list[2])
    r_year = int(r_list[0])
    r_month = int(r_list[1])
    r_day = int(r_list[2])
    num = 0

    while True:
        if j_year == r_year and j_month == r_month:
            num += r_day - j_day + 1
            break
        else:
            if (j_year % 4 == 0 and j_year % 100 != 0) or j_year % 400 == 0:
                num += days2[j_month] - j_day + 1
                j_day = 1
                j_month += 1
                if j_month == 13:
                    j_month = 1
                    j_year += 1
            else:
                num += days[j_month] - j_day + 1
                j_day = 1
                j_month += 1
                if j_month == 13:
                    j_month = 1
                    j_year += 1
    print(num)

    # 일요일 계산
    j_year = int(j_list[0])
    j_month = int(j_list[1])
    j_day = int(j_list[2]) + goto_SUN(j_list[3])
    r_year = int(r_list[0])
    r_month = int(r_list[1])
    r_day = int(r_list[2])

    while True:

        if j_year == r_year and j_month == r_month and j_day>r_day:
            break

        if (j_year % 4 == 0 and j_year % 100 != 0) or j_year % 400 == 0:

            if j_day > days2[j_month]:
                if j_month == 12:
                    j_year += 1
                    j_day -= days2[j_month]
                    j_month = 1

                else:
                    j_day -= days2[j_month]
                    j_month += 1
        else:
            if j_day > days[j_month]:
                if j_month == 12:
                    j_year += 1
                    j_day -= days[j_month]
                    j_month = 1

                else:
                    j_day -= days[j_month]
                    j_month += 1

        if j_day < 10 and j_month < 10:
            h_str = str(j_year) + '0' + str(j_month) + '0' + str(j_day)
        elif j_day < 10:
            h_str = str(j_year) + str(j_month) + '0' + str(j_day)
        elif j_month < 10:
            h_str = str(j_year) + '0' + str(j_month) + str(j_day)
        else:
            h_str = str(j_year) + str(j_month) + str(j_day)

        answer.append(h_str)
        j_day += 7

    #토요일 계산
    j_year = int(j_list[0])
    j_month = int(j_list[1])
    j_day = int(j_list[2]) + goto_SAT(j_list[3])
    r_year = int(r_list[0])
    r_month = int(r_list[1])
    r_day = int(r_list[2])

    while True:

        if j_year == r_year and j_month == r_month and j_day>r_day:
            break

        if j_year % 4 == 0 and j_year % 100 != 0:   #윤달

            if j_day > days2[j_month]:
                if j_month == 12:
                    j_year += 1
                    j_day -= days2[j_month]
                    j_month = 1

                else:
                    j_day -= days2[j_month]
                    j_month += 1
        else:
            if j_day > days[j_month]:
                if j_month == 12:
                    j_year += 1
                    j_day -= days[j_month]
                    j_month = 1

                else:
                    j_day -= days[j_month]
                    j_month += 1


        if j_day < 10 and j_month < 10:
            h_str = str(j_year) + '0' + str(j_month) + '0' + str(j_day)
        elif j_day < 10:
            h_str = str(j_year) + str(j_month) + '0' + str(j_day)
        elif j_month < 10:
            h_str = str(j_year) + '0' + str(j_month) + str(j_day)
        else:
            h_str = str(j_year) + str(j_month) + str(j_day)

        answer.append(h_str)
        j_day += 7


    #공휴일 계산
    r_date = int(r_list[0] + r_list[1]+r_list[2])
    j_date = int(j_list[0]+j_list[1] + j_list[2])

    for a in range(len(holidays)):
        year = int(j_list[0])
        h_month = holidays[a].split("/")[0]
        h_day = holidays[a].split("/")[1]


        while True:

            h_date = int(str(year) + h_month + h_day)


            if h_date <= r_date and j_date <= h_date:
                if str(h_date) not in answer:
                    answer.append(str(h_date))
                    print(h_date)

            elif year > r_year:

                break
            year += 1



    answer.sort()
    print(answer)
    return num - len(answer)

a = "2020/01/05 TUE"
b = "2024/03/20"
c = ["05/05", "12/25", "03/01"]
print(solution(a,b,c))
