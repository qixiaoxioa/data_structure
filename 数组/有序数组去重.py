class Solution1:
    def removeDuplication(self,nums:list)-> int:
        fast = 1
        slow = 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
            else:
                fast += 1
        return slow + 1
s = Solution1()
nums = [1,1,2,2,3,4,5]
print(s.removeDuplication(nums))

