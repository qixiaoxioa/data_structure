def BinarySearchTree(nums:list,val:int):
    left = 0
    right = len(nums) - 1
    if val == nums[left]:
        return left
    elif val == nums[right]:
        return right
    else:
        mid = (left + right)//2
        if val >= nums[mid]:
            left = mid
        elif val <nums[mid]:
            right = mid
        else:
            return mid
nums = [0,2,5,10,15,20,23,89,100]
print(BinarySearchTree(nums,89))