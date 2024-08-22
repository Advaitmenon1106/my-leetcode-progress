def plusOne(digits: list[int]) -> list[int]:
    num = ''
    for i in range(0, len(digits)):
        num+=str(digits[i])
        
    res = int(num)+1
    return [int(i) for i in list(str(res))]