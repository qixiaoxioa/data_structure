"""
:Author:小七
:CREAT:2020/10/10 11:09
"""
class Node:
    def __init__(self,data):
        self.val = data
        self.next = None
    # def __repr__(self):
    #     return f"Node({self.val})"

class Solution:
    def removeElement(self,head:Node,val:int):
        dummy = Node(0)
        dummy.next = head
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                temp =curr.next
                curr.next = curr.next.next
                temp.next = Node
            else:
                curr = curr.next
        return dummy.next
    def print_list(self,head):
        curr = head
        string = ""
        while curr:
            string += f"{curr.val}-->"
            curr = curr.next
        return string


if __name__ == '__main__':
    node1 = Node(0)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(3)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = None
    s = Solution()
    s.removeElement(node1,3)
    print(s.print_list(node1))












