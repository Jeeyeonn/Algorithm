plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]

plans.sort(key = lambda x :(x[1]))
answer, remain = [], []
pre = plans[0]
for i in range(1, len(plans)):
    pre_end_h = int(pre[1].split(':')[0])
    pre_end_m = int(pre[1].split(':')[1]) + int(pre[2])
    while pre_end_m >= 60:
        pre_end_m -= 60
        pre_end_h += 1
    pre_end_time = pre_end_h * 100 + pre_end_m
    
    cnt_end_h = int(plans[i][1].split(':')[0])
    cnt_end_m = int(plans[i][1].split(':')[1])
    if cnt_end_m >= 60:
        cnt_end_m -= 60
        cnt_end_h += 1
    cnt_end_time = cnt_end_h * 100 + cnt_end_m

    if cnt_end_time < pre_end_time:
        remain.append([pre[0], (pre_end_h - cnt_end_h)*60 + (pre_end_m-cnt_end_m)])
        pre = plans[i]
    elif cnt_end_time == pre_end_time:
        answer.append(pre[0])
        pre = plans[i]
    else:
        answer.append(pre[0])
        remain_time = (cnt_end_h - pre_end_h)*60 + (cnt_end_m-pre_end_m)
        while True:
            if len(remain) == 0:
                break
            relate_remain = remain.pop()
            if relate_remain[1] <= remain_time:
                answer.append(relate_remain[0])
                remain_time -= relate_remain[1]
            else:
                remain.append([relate_remain[0], relate_remain[1] - remain_time])
                pre = plans[i]
                break
    if i == len(plans) - 1:
        answer.append(pre[0])



while len(remain) != 0:
    r = remain.pop()
    answer.append(r[0])

print(answer)