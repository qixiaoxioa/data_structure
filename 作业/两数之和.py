# class Solution:
#     def twoSums(self,nums,target):
#         for i in range(len(nums)):
#             if target - nums[i] in nums and i != nums.index(target - nums[i]):
#                 return i,nums.index(target - nums[i])


class Solution:
	# def twoSum(self,nums,target):
	# 	d = {}
	# 	n = len(nums)
	# 	for x in range(n):
	# 		if target - nums[x] in d:
	# 			return d[target-nums[x]],x
	# 		else:
	# 			d[nums[x]] = x

	# ==========暴力拆解===============c
	def twoSum(self,nums,target):
		for i in range(len(nums)):
			for j in nums[i+1:]:
				if nums[i] + j == target:
					print(i,nums.index(j))


nums = [1,1,8,10,5]
s = Solution()
s.twoSum(nums,9)

