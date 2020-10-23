class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"
def changeNodes(head):
   dummy = Node(0)
   pre = dummy
   dummy.next = head
   while pre.next and pre.next.next:
       slow = pre.next
       fast =pre.next.next
       pre.next = fast
       slow.next =fast.next
       fast.next = slow
       pre = pre.next.next
   return dummy.next

def pprint(head):
    current = head
    string = ""
    while current:
        string += f"{current}-->"
        current = current.next
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
    print(pprint(changeNodes(node1)))

