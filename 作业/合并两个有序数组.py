def Twoarray(nums1:list,m:int,nums2:list,n:int):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        elif nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            j -=1
        k -= 1
    while i >= 0:
        nums1[k] = nums1[i]
        k -= 1
        i -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1
    return nums1
nums1 = [1,2,3,8]
nums2 = [2,3,5,10]
print(Twoarray(nums1,4,nums2,4))

