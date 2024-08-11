def removeElement(nums: list[int], val: int) -> int:
    new_arr = []
    for _, n in enumerate(nums):
        if n == val:
            continue
        else:
            new_arr.append(n)
    nums[:] = new_arr[:]
    del new_arr
    return len(nums)