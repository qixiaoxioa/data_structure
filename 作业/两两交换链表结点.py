class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"
class Revolution:
    def changePoint(self,head):
        dummy = Node(0)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            slow = pre.next
            fast = pre.next.next
            pre.next = fast
            slow.next = fast.next
            fast.next = slow
            pre = pre.next.next
        return dummy.next
    def print_list(self,head):
        curr = head
        string = ""
        while curr:
            string += f"{curr}-->"
            curr = curr.next
        return string
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None

    r = Revolution()
    a = r.changePoint(node1)
    print(r.print_list(a))




