def maxDistance(arrays: list[list[int]]) -> int:
    maxVals = []
    minVals = []
    tracker = []
    for arr in arrays:
        maxVals.append(arr[-1])
        minVals.append(arr[0])
        if len(arr)!=1:
            tracker.append(set((arr[-1], arr[0])))
        
    sortedMaxVals = sorted(maxVals)
    sortedMinVals = sorted(minVals, reverse=True)
    while True:
        print(len(sortedMinVals))
        minVal = sortedMinVals[-1]
        maxVal = sortedMaxVals[-1]
        if set([minVal, maxVal]) not in tracker:
            return maxVal-minVal
        else:
            sortedMinVals.pop()
            sortedMaxVals.pop()

print(maxDistance([[1],[1]]))


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maxVals = []
        minVals = []
        for i, k in enumerate(arrays):
            maxVals.append((k[-1], i))
            minVals.append((k[0], i))
        
        sortedMaxVals = sorted(maxVals, key=lambda x: x[0], reverse=True)
        maxVal, arrayNumber_max = sortedMaxVals[0]
        sortedMinVals = sorted(minVals, key=lambda x:x[0], reverse=True)

        while True:
            minVal, arrayNumber_min = sortedMinVals[-1]
            if arrayNumber_max!=arrayNumber_min:
                return maxVal - minVal
            else:
                sortedMinVals.pop()