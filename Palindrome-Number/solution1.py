def isPalindrome(self, x: int) -> bool:
    stringOfNumber = list(str(x))
    reverse = stringOfNumber[::-1]
    return reverse == stringOfNumber