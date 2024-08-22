def mySqrt(x: int) -> int:
        if x == 0: return 0
        if x == 1: return 1
        for i in range(0, int((x//2))+1):
            if i**2 < x and (i+1)**2 > x:
                return i
            
print(mySqrt(31))