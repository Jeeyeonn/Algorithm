#프로그래머스 : 오픈채팅방

def solution(record):
    record_list = []
    answer = []

    for a in record:
        b = a.split()
        b[1] = b[1][3:]
        record_list.append(b)

    user = dict()

    for a in record_list:
        if a[0] == 'Enter' or a[0] == 'Change':
           user[a[1]] = a[2]

    for a in record_list:
        if a[0] == 'Enter':
            nickname = user[a[1]]
            a_str = nickname+'님이 들어왔습니다.'
            answer.append(a_str)
        elif a[0] == 'Leave':
            nickname = user[a[1]]
            a_str = nickname + '님이 나갔습니다.'
            answer.append(a_str)

    return answer

p = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(p))