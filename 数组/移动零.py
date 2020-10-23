# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

class Solution2:
    def removeZero(self,nums):
        fast = 0  #找到非零元素
        slow = 0
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        for i in range(slow,len(nums)):
            nums[i] = 0
        return nums
s2 = Solution2()
nums = [1,2,0,4,3,0]
print(s2.removeZero(nums))


