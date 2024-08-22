def lengthOfLastWord(self, s: str) -> int:
    s = s[::-1]
    s = s.split()
    return len(s[0])
