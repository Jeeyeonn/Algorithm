def solution(registered_list, new_id):

    if new_id not in registered_list:
        return new_id
    else:
        index = len(new_id)
        for i in range(len(new_id)):
            if new_id[i].isdigit():
                index = i
                break

        new_s = new_id[:index]
        new_n = new_id[index:]
        if len(new_id[index:]) == 0:
            new_n = 0
        else:
            new_n = int(new_n)

        num = []
        for j in registered_list:
            if new_s in j:
                j_num = j[len(new_s):]
                if len(j_num) == 0:
                    j_num = '0'
                num.append(int(j_num))

        while True:
            if new_n not in num:
                break
            else:
                new_n += 1


    return new_s+str(new_n)

a = ["cow", "cow1", "cow2", "cow3", "cow4", "cow5", "cow6", "cow7" ,"cow8", "cow9"]
b = "cow"
print(solution(a,b))