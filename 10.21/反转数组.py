# 反转数组
def reverseArray(nums:list):
    begin = 0
    end = len(nums) - 1
    while begin < end:
        c = nums[begin]
        nums[begin] = nums[end]
        nums[end] = c
        begin += 1
        end -= 1
    return nums
nums = [1,2,5,4,8,7]
print(reverseArray(nums))

# 反转链表
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"
def reverseLink(head):
    dummy = Node(0)
    pre = dummy
    cur = head
    while cur:
        node = cur.next

