def solution(phone_book):
    size = len(phone_book)
    for i in range(size-1):
        i_len = len(phone_book[i])
        for j in range(i+1, size):
            if i_len <= len(phone_book[j]) and phone_book[i] == phone_book[j][:i_len]:
                return False

    return True

def solution2(phone_book):
    size = len(phone_book)
    phone_book.sort()

    for i in range(size-1):
        j = i+1
        num = phone_book[i]
        while True:
            if num == phone_book[j][:len(num)]:
                return False
            else:
                if len(num) < len(phone_book[j]) or num != phone_book[j][:len(phone_book)]:
                    num = phone_book[j]
                    break
            j += 1

    return True

a = ["119", "97674223", "1195524421"]
b = ["123", "456", "789"]
c = ["12", "123", "1235", "567", "88"]

print(solution2(a))