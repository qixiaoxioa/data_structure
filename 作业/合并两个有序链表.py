class Node:
    def __init__(self,val):
        self.val= val
        self.next = None
    def __repr__(self):
        return f"{self.val}"
class Soultion:
    def mergeTwoLists(self,l1:Node,l2:Node):
        dummy = Node(0)
        curr = dummy
        while l1 or l2:
            if l1 is None:
                curr.next = l2
                break
            if l2 is None:
                curr.next = l1
                break
            if l1.val < l2.val:
                curr.next = Node(l1.val)
                l1 = l1.next
            else:
                curr.next = Node(l2.val)
                l2 = l2.next
            curr = curr.next
        return dummy.next
def print_list(head):
    curr = head
    string = ""
    while curr:
        string += f"{curr}-->"
        curr = curr.next
    return string + "END"
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(5)
    node4 = Node(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None
    node5 = Node(2)
    node6 = Node(4)
    node7 = Node(6)
    node8 = Node(8)
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = None
    s = Soultion()
    print(print_list(s.mergeTwoLists(node1,node5)))



