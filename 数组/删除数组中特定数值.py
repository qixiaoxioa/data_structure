class Solution:
    def removeElement(self,nums,val):
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        return nums[:slow],slow
s = Solution()
nums = [1,4,1,2,3,4]
print(s.removeElement(nums,1))
