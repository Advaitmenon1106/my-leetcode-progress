
def twoSum(nums: list[int], target: int) -> list[int]:
    for i, n in enumerate(nums):
        n1 = n
        for j, n2 in enumerate(nums):
            if i!=j and target-n1 == n2:
                return [i, j]
