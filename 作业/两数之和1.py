

def twoSum(nums,target):
    nums.sort()
    begin = 0
    end = len(nums) - 1
    while begin < end:
        sum = nums[begin] + nums[end]
        if sum == target:
            print(begin,nums[begin],end,nums[end])
            begin += 1
            end -= 1
        else:
            if sum < target:
                begin += 1
            else:
                end -= 1
nums = [1,5,4,2,3]
twoSum(nums,8)