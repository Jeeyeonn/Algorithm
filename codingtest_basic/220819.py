import sys

def solution(s):
    answer = sys.maxsize
    s_list = list(s)

    for a in range(1, len(s_list) // 2 + 1):
        c_list = ""
        cut = ""  # 전 문자
        num = 0  # 몇번 반복인지?
        b = 0
        while b < len(s_list):

            if cut == "".join(s_list[b:b + a]):
                num += 1
            else:
                if cut != "":
                    if num == 0:
                        c_list += "".join(cut)
                        cut = s_list[b:b + a]
                        cut = "".join(cut)

                    else:
                        str_num = str(num+1)
                        c_list += str_num + "".join(cut)
                        num = 0
                        cut = s_list[b:b + a]
                        cut = "".join(cut)
                else:
                    cut = s_list[b:b + a]
                    cut = "".join(cut)

            b += a
        if num == 0:
            c_list += "".join(cut)
        else:
            str_num = str(num + 1)
            c_list += str_num + "".join(cut)

        answer = min(answer, len(c_list))
        print(c_list)

    return answer


p = "aabbaccc"
print(solution(p))