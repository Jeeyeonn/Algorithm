n = int(input())

if n < 25:
    print(n//5)
elif 25 >= n and n < 125:
    print(n//5 + 1)
else:
    print(n//5 + 2)