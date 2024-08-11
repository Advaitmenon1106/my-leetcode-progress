def remove_duplicates(nums) -> int:
    nums[:] = sorted(list(set(nums)))
    return len(nums)
