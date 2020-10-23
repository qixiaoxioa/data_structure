
# def TwoSum(nums:list,target):
#     nums.sort()
#     begin = 0
#     end = len(nums) - 1
#     while begin < end:
#         sum = nums[begin] + nums[end]
#         if  sum== target:
#             print(begin,end)
#             begin += 1
#             end -= 1
#         else:
#             if sum < target:
#                 begin += 1
#             else:
#                 begin -= 1


# def TwoSum(nums,target):
#     for i in range(len(nums)):
#         for j in range(i + 1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return i,j

def TwoSum(nums:list,target):
    d ={}
    for i in range(len(nums)):
        temp = target -  nums[i]
        if temp in d:
            return d[temp],i
        d[nums[i]] = i

nums = [1,4,3,5,2]
print(TwoSum(nums,6))