def isValid(s: str) -> bool:
    stack = []
    head = -1

    bracket_pairs = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    closing_brackets = set(bracket_pairs.keys())
    opening_brackets = set(['{', '(', '['])

    expression_arr = list(s)
    for ch in expression_arr:
        if head == -1 and ch in closing_brackets:
            return False
        if head != -1 and ch in closing_brackets:
            if stack[head] == bracket_pairs[ch]:
                stack.pop()
                head -= 1
            else:
                return False
        elif ch in opening_brackets:
            stack.append(ch)
            head+=1

    return len(stack) == 0
