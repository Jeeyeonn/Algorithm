from typing import List


def solution(k: int, dic: List[str], chat: str) -> str:
    answer = chat

    for i in range(len(dic)):
        a = chat.split(" ")

        for j in a:
            # print(j)
            b = j.split(".")

            result = True
            count = len(b) -1  #점의 갯수
            num = 0

            for h in b:

                if h in dic[i]:
                    if h == '':
                        fffcount = 1
                    else:
                        num += len(h)
                else:
                    result = False
                    break


            if k != 0:
                if num + count <= len(dic[i]) <= num + (count * k):
                    ince = 0
                else:
                    result = False

            if result:
                b = '#' * len(j)
                answer = answer.replace(j, b)

    return answer

a = ["slang", "badword"]
b = "badword ab.cd bad.ord .word sl.. bad.word"
print(solution(2, a,b))