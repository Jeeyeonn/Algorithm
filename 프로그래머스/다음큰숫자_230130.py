def solution(n):
    bin_num = list(bin(n)[2:])
    if bin_num.count("0") == 0:
        bin_num = bin_num[:1] + ["0"] + bin_num[1:]
    elif bin_num[0] == "1" and bin_num[1:].count("1") == 0:
        return n * 2
    elif (
        bin_num[len(bin_num) - 1] == "0" and bin_num[: len(bin_num) - 1].count("0") == 0
    ):
        bin_num = ["1", "0", "0"] + list("1" * (bin_num.count("1") - 1))
    else:
        str_num = "".join(bin_num)
        str_list = len(str_num.split("01")) - 1
        cnt = 0
        for i in range(1, len(bin_num)):
            if bin_num[i] == "0" and bin_num[i + 1] == "1":
                cnt += 1
                if cnt == str_list:
                    bin_num[i] = "1"
                    bin_num[i + 1] = "0"
                    one_count = bin_num[i + 2 :].count("1")
                    bin_num = bin_num[: i + 2] + list(
                        "0" * ((len(bin_num[i + 2 :])) - one_count) + ("1" * one_count)
                    )
                    break
    bin_num = "".join(bin_num)
    return int(bin_num, 2)


print(solution(78))
print(solution(42))
print(solution(15))
print(solution(8))
print(solution(6))
