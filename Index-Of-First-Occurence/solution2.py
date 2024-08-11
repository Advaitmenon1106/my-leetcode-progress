def strStr(self, haystack: str, needle: str) -> int:
    first_letter = needle[0]
    len_of_needle = len(needle)

    for i in range(0, len(haystack)):
        if haystack[i] == first_letter and haystack[i:i+len_of_needle] == needle:
            return i
    return -1