def romanToInt(s: str) -> int:
    defaultNos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    no = 0
    for i in range(0, len(s)-1):
        val = s[i]
        nextVal = s[i+1]
        if defaultNos[nextVal]>defaultNos[val]:
            no = no-defaultNos[val]
        else:
            no+=defaultNos[val]

    return no+defaultNos[s[-1]]
