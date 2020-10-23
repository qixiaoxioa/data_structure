# def threeSum(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+ 1,len(nums)):
#             for k in range(i + 2,len(nums)):
#                 if nums[i] + nums[j] + nums[k] == target:
#                     return i,j,k
# nums = [1,3,5,7,4,6,2,2,3]
# print(threeSum(nums,6))

# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
def ThreeSum(nums):
    nums.sort()
    a = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i]== nums[i - 1]:
            continue
        begin = i + 1
        end = len(nums) - 1
        while begin < end:
            if nums[i] + nums[begin] + nums[end] < 0:
                begin += 1
            elif nums[i] + nums[begin] + nums[end] >0:
                end -= 1
            else:
                a.append([nums[i],nums[begin],nums[end]])
                while begin <end and nums[begin] == nums[begin + 1]:
                    begin += 1
                while begin < end and nums[end] == nums[end -1]:
                    end -= 1
                begin += 1
                end -= 1
    return a
nums = [-2,-1,0,1,3,4]
print(ThreeSum(nums))