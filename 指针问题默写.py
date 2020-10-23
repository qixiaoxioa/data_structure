# 两数之和
# 1.暴力法
def twoSum(nums,target):
    for i in range (len(nums)):
        for j in range(i + 1,len(nums)):
            if nums[i] + nums[j] == target:
                return i,j

# 2.快慢指针
def twoSum1(nums:list,target):
    nums.sort()
    begin = 0
    end = len(nums) - 1
    while begin < end:
        sums = nums[begin] + nums[end]
        if sums == target:
            begin += 1
            end += 1
        else:
            if sums < target:
                begin += 1
            else:
                end -= 1
    return begin,end



