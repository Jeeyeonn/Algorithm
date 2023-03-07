
def solution(s):
    stack = []
    answer = True
    
    for i in s:
        if len(stack) == 0:
            if i == '(':
                stack.append(i)
            else:
                return False
        else:
            if i == '(':
                stack.append(i)
            else:
                stack.pop()
    if len(stack) != 0:
        return False
    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))