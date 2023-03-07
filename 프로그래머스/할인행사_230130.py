def solution(want, number, discount):
    answer = 0

    for day in range(len(discount) - 9):
        day_list = discount[day : day + 10]
        for n in range(len(want)):
            if day_list.count(want[n]) < number[n]:
                break
        else:
            answer += 1

    return answer


print(
    solution(
        ["banana", "apple", "rice", "pork", "pot"],
        [3, 2, 2, 2, 1],
        [
            "chicken",
            "apple",
            "apple",
            "banana",
            "rice",
            "apple",
            "pork",
            "banana",
            "pork",
            "rice",
            "pot",
            "banana",
            "apple",
            "banana",
        ],
    )
)
print(
    solution(
        ["apple"],
        [10],
        [
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
        ],
    )
)
