class Solution:
    def removeDuplicats(self,nums:list) -> int:
        fast = 1
        slow = 0
        count = 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                count += 1
                if count == 2:
                    slow += 1
                    nums[slow] = nums[fast]
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
                count = 1
        return nums[:slow + 1],slow + 1
s = Solution()
nums = [1,1,1,1,2,2,3,4]
print(s.removeDuplicats(nums))