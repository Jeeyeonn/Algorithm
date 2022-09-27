def solution(commands):
    answer = []
    final = []
    merge = []
    for _ in range(50):
        num = []
        for _ in range(50):
            num.append('0')
        answer.append(num)


    for i in commands:
        s = i.split(" ")

        if len(s) == 4:
            inputs = i.split(" ")[0]
            x = int(i.split(" ")[1])
            y = int(i.split(" ")[2])
            name = i.split(" ")[3]

            if inputs == 'UPDATE':
                reesult = True
                kkkkey = str(x) + ':' + str(y)
                for k in range(len(merge)):
                    if kkkkey in merge[k]:
                        reesult = False
                        merge[k] = merge[k].split(" ")[0] + ' ' + name
                if reesult:
                    answer[x][y] = name

        elif len(s) == 3:
            inputs = i.split(" ")[0]
            x = i.split(" ")[1]
            name = i.split(" ")[2]

            if inputs == 'UPDATE':

                for a in range(len(answer)):
                    for b in range(len(answer[a])):
                        if answer[a][b] == x:
                            answer[a][b] = name

            elif inputs == 'PRINT':
                rresult = True
                kkkey = x + ':' + name
                for aaa in merge:
                    if kkkey in aaa:
                        rresult = False
                        final.append(aaa.split(" ")[1])
                if rresult:
                    if answer[int(x)][int(name)] == '0':
                        final.append('EMPTY')
                    else:
                        final.append(answer[int(x)][int(name)])

            elif inputs == 'UNMERGE':
                kkey = x + ':' + name
                for a in range(len(merge)):
                    if kkey in merge[a]:
                        m_list = merge[a].split(" ")[0].split("/")
                        nnum = merge[a].split(" ")[1]
                        for mm in m_list:
                            xx = int(mm.split(":")[0])
                            yy = int(mm.split(":")[1])
                            answer[xx][yy] = '0'
                        merge[a] = ''
                        answer[int(x)][int(name)] = nnum

        else:
            inputs = i.split(" ")[0]
            x = int(i.split(" ")[1])
            y = int(i.split(" ")[2])
            dx = int(i.split(" ")[3])
            dy = int(i.split(" ")[4])

            if inputs == 'MERGE':
                key = str(x) + ':' + str(y)
                result = False
                for i in range(len(merge)):
                    if key in merge[i]:
                        result = True
                        merge[i] = merge[i].split(" ")[0] + '/' + str(dx) + ':' + str(dy) + ' ' + merge[i].split(" ")[1]
                        p = str(dx) + ':' + str(dy)

                        for j in range(len(merge)):
                            if p in merge[j] and key not in merge[j]:
                                merge[j] = merge[j].split(" ")[0].replace(p, "")
                                first = merge[i].split(" ")[0]
                                merge[i] = first + merge[j] + ' ' + merge[i].split(" ")[1]
                                merge[j] = ''

                if result == False:
                    key = str(x) + ':' + str(y) + '/' + str(dx) + ':' + str(dy) + ' ' + answer[x][y]
                    merge.append(key)

    return final

a = ["UPDATE 1 1 menu", "UPDATE 1 2 category",
     "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean",
     "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean",
    "UPDATE 3 3 noodle", "UPDATE 3 4 instant",
     "UPDATE 4 1 pasta", "UPDATE 4 2 italian",
     "UPDATE 4 3 noodle", "MERGE 1 2 1 3",
     "MERGE 1 3 1 4", "UPDATE korean hansik",
     "UPDATE 1 3 group", "UNMERGE 1 4",
    "PRINT 1 3", "PRINT 1 4"]
b = ["UPDATE 1 1 a", "UPDATE 1,2 b", "UPDATE 2 1 C",
    "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1",
    "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]

print(solution(a))