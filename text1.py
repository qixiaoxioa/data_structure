class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"
class Solution:
    def twoChangePoint(self,s1:Node,s2:Node):
        dummy = Node(0)
        pre = dummy
        while s1 or s2:
            if s1.data < s2.data:
                pre.next = Node(s1.data)
                s1 = s1.next
            else:
                pre.next = Node(s2.data)
                s2 = s2.next
            if s1 is None:
                pre.next = s2
                break
            if s2 is None:
                pre.next = s2
                break
        return dummy.next
    def twoChangePoint2(self,s1:Node,s2:Node):
        dummy = Node(0)
        pre = dummy
        while s1 and s2:
            if s1.data < s2.data:
                pre.next = Node(s1.data)
                s1 = s1.next
            else:
                pre.next = Node(s2.data)
                s2 = s2.next
        if s1 is None:
            pre.next = s2
        if s2 is None:
            pre.next = s1

class stackArray:
    def __init__(self):
        self.stack = []
        self.size = 0
    # 压栈
    def push(self,data):
        self.stack.append(data)
        self.size += 1
    # 弹栈
    def pop(self):
        if self.stack:
            temp = self.stack.pop()
            self.size -= 1
            return temp
        else:
            raise IndexError("下标越界")
#
