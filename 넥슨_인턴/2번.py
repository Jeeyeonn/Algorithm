def getMaximumRemovals(order, source, target):
    answer = 0
    target_list = list(target)
    for i in order:
        source = source[:i-1] + "_" + source[i:]
        copy_source = source
        for j in target_list:
            if j in copy_source:
                index = copy_source.index(j)
                copy_source = copy_source[:index] + "_" + copy_source[index+1:]
            else:
                return answer
        answer += 1


if __name__ == '__main__':
    order_count = int(input().strip())
    order = []

    for _ in range(order_count):
        order_item = int(input().strip())
        order.append(order_item)

    source = input()

    target = input()

    result = getMaximumRemovals(order, source, target)
    print(result)