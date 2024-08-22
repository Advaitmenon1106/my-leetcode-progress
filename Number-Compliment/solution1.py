def findComplement(self, num: int) -> int:
    binary_rep = bin(num)[2:]
    complement_binary = ''
    for c in binary_rep:
        if c == '1':
            complement_binary+='0'
        else:
            complement_binary+='1'
        
    return int(complement_binary, 2)