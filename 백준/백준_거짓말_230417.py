n, m = list(map(int, input().split()))
know_person = list(map(int, input().split()))
person = {}
if len(know_person) != 1:
    know_person = know_person[1:]
    for i in know_person:
        person[i] = False
else:
    print(m)

party = {}
n_party = []

answer = 0
for i in range(m):
    num = list(map(int, input().split()))[1:]
    is_ok = True
    for n in num:
        if n in person and not person[n]:
            is_ok = False
            break
    if is_ok:
        answer += 1
        for n in num:
            if n in person:
                person[n].append(i)
            else:
                person[n] = [i]
    else:
        minus = []
        for n in num:
            if n not in person:
                person[n] = False
            elif person[n] != False:
                minus += person[n]
        answer -= len(set(minus))
print(answer)

