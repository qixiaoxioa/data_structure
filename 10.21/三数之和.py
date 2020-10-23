def threeSum(nums:list,target):
    a = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i]== nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sums = nums[i] + nums[left] + nums[right]
            if sums < target:
                left += 1
            elif sums > target:
                right -= 1
            else:
                a.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return a
nums = [-2,-1,0,1,3,4]
print(threeSum(nums,5))
