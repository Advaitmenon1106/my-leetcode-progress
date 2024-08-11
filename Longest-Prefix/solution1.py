
def longestCommonPrefix(strs: List[str]) -> str:
    pref = ''
    if len(strs) == 0:
        return ''
    elif len(strs) == 1:
        return strs[0]
    smallestWord = sorted(strs, key=len)[0]
    count = 0
    word = ''
    for i in range(len(smallestWord)):
        for word in sorted(strs, key=len)[1:]:
            if word[i] == smallestWord[i]:
                count+=1
            else:
                break
        if word[i]!=smallestWord[i]: 
            break
        if count == len(strs)-1:
            pref+=smallestWord[i]
        count = 0
    return pref
