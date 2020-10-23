def ReverseArray(nums):
    begin = 0
    end = len(nums) - 1
    while begin < end:
        c = nums[begin]
        nums[begin] = nums[end]
        nums[end] = c
        begin += 1
        end -= 1
        if begin == end:
            nums[begin] = nums[end]
    return nums
nums = [3,2,5,4,8,7]
print(ReverseArray(nums))

