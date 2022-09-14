import math

def is_Decimal(a):
    aa = int(a)
    for i in range(2, int(math.sqrt(aa)+1)):
        if aa % i == 0:
            return False
    return True


for _ in range(int(input())):
    num = int(input())

    a, b = num//2, num//2
    while a > 0:
        if is_Decimal(a) and is_Decimal(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1