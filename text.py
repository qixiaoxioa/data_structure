# 删除有序数组重复项(最多保留两个)
# class Solution:
#     def removeDuplicates(self,nums:list):
#         fast = 1
#         slow = 0
#         count = 1
#         while fast < len(nums):
#             if nums[fast] == nums[slow]:
#                 count += 1
#                 if count == 2:
#                     slow += 1
#                     nums[slow] = nums[fast]
#                 fast += 1
#             else:
#                 slow += 1
#                 nums[slow] = nums[fast]
#                 fast += 1
#                 count = 1
#         return nums[:slow+1],slow + 1
# S = Solution()
# nums = [1,1,1,1,2,2,3,4]
# print(S.removeDuplicates(nums))

# 删除数组中特定值
# class Solution:
#     def Removepoints(self,nums:list,var):
#         slow = 0
#         fast = 0
#         while fast < len(nums):
#             if nums[fast] != var:
#                 nums[slow] = nums[fast]
#                 slow += 1
#             fast += 1
#         return slow,nums[:slow]
# S = Solution()
# nums = [0,1,0,2,4,5]
# print(S.Removepoints(nums,0))

# 移动零
# class Solution:
#     def Removezeros(self,nums:list):
#         slow = 0
#         fast = 0
#         while fast < len(nums):
#             if nums[fast] == 0:
#                 fast += 1
#             else:
#                 nums[slow] = nums[fast]
#                 slow += 1
#                 fast += 1
#         for i in range(slow,len(nums)):
#             nums[i] = 0
#
#         return nums,slow
# S = Solution()
# nums = [0,1,0,2,4,5]
# print(S.Removezeros(nums))

# 删除有序数组重复项
# class Solution:
#     def removeDuplicate(self,nums:list):
#         fast = 1
#         slow = 0
#         while fast < len(nums):
#             if nums[slow]!=nums[fast]:
#                 slow += 1
#                 nums[slow] = nums[fast]
#                 fast += 1
#             else:
#                 fast += 1
#         return nums,slow + 1
# S = Solution()
# nums = [1,1,1,1,2,2,3,4]
# print(S.removeDuplicate(nums))

# 栈--数组
class Stack:
    def __init__(self,limit:10):
        self.stack = []
        self.size = 0
#     压栈
    def __str__(self):
        return str(self.stack)
    def push(self,data):
        self.stack.append(data)
        self.size += 1
# 弹栈
    def pop(self):
        if self.stack:
            temp = self.stack.pop()
            self.size -= 1
        else:
            raise IndexError("")
        return temp
    def peek(self):
        if self.size == 0:
            raise IndexError("xxx")
        else:
            return self.stack[-1]


#    栈--列表
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"node({self.data})"

class stackoflink:
    def __init__(self):
        self.top = None
        self.size = 0
#     压栈
    def push(self, val):
        node  =Node(val)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1
#     弹栈
    def pop(self):
        if self.top is None:
            raise IndexError("索引越界")
        else:
            remove = self.top
            self.top = self.top.next
            remove.next = None
            self.size -= 1
        return remove










