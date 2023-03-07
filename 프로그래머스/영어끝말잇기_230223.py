def solution(n, words):
    answer = {}
    if len(words[0]) == 1:
        return [1, 1]
    answer[words[0][0]] = [words[0]]
    for idx in range(1, len(words)):
        if len(words[idx])==1 or words[idx][0] != words[idx-1][-1]:
                one = (1+idx)//n if (1+idx)%n==0 else (1+idx)%n
                two = (1+idx)//n if (1+idx)%n==0 else (1+idx)//n+1
                return [one, two]


        if answer.get(words[idx][0]) == None:
            answer[words[idx][0]] = [words[idx]]
        else:
            if words[idx] in answer[words[idx][0]]:
                one = (1+idx)//n if (1+idx)%n==0 else (1+idx)%n
                two = (1+idx)//n if (1+idx)%n==0 else (1+idx)//n+1
                return [one, two]
            else:
                answer[words[idx][0]].append(words[idx])
    return [0, 0]


# print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
# print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
print(solution(5,  ["aba", "asa", "s"]))