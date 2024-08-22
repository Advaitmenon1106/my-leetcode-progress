def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        newList = []
        i = 0
        j = 0
        while i<m or j<n:
            print(i, j)
            if i == m-1:
                 newList.append(nums1[i])
                 newList.extend(nums2[j:])
                 break
            elif j == n-1:
                 newList.append(nums1[j])
                 newList.extend(nums1[i:])
                 break
            else:
                pointer_nums1 = nums1[i]
                pointer_nums2 = nums2[j]
                if pointer_nums1<pointer_nums2:
                    newList.append(pointer_nums1)
                    i+=1
                elif pointer_nums2<pointer_nums1:
                    newList.append(pointer_nums2)
                    j+=1
                elif pointer_nums1 == pointer_nums2:
                    newList.append(pointer_nums1)
                    newList.append(pointer_nums2)
                    i+=1
                    j+=1
        
        print(newList)
        nums1 = newList

merge([1, 2, 3], 3, [2, 5, 6], 3)